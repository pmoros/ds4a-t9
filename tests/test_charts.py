"""AC7: chart builders and the filters that feed them, on small synthetic frames."""

import pandas as pd
import pytest

from dashboard import charts
from dashboard.callbacks.travelers import menu_loader


def _travelers():
    rows = [
        # AÑO, MES, ORIGEN, SUBTEMA, ITEM, VIAJEROS
        (2019, "ENERO", "BOGOTA", "EDAD", "B. 18-24", 10),
        (2019, "ENERO", "BOGOTA", "EDAD", "A. NS/NR", 99),
        (2019, "TOTAL", "BOGOTA", "EDAD", "B. 18-24", 500),
        (2019, "FEBRERO", "META", "EDAD", "B. 18-24", 5),
        (2020, "ENERO", "BOGOTA", "EDAD", "B. 18-24", 7),
        (2019, "ENERO", "BOGOTA", "GENERO", "A. HOMBRE", 3),
    ]
    columns = ["AÑO", "MES", "ORIGEN", "SUBTEMA", "ITEM", "VIAJEROS"]
    return pd.DataFrame(rows, columns=columns)


def test_subtopic_filter_drops_total_and_not_known():
    frame = charts.travelers_subtopic(_travelers(), "EDAD", ["2019"], not_known="A. NS/NR")
    assert list(frame["VIAJEROS"]) == [10, 5]
    assert set(frame["SUBTEMA"]) == {"EDAD"}


def test_subtopic_filter_keeps_not_known_when_not_asked():
    frame = charts.travelers_subtopic(_travelers(), "EDAD", [2019])
    assert list(frame["VIAJEROS"]) == [10, 99, 5]


def test_subtopic_filter_by_origin_and_years_as_strings():
    frame = charts.travelers_subtopic(_travelers(), "EDAD", ["2019", "2020"], origins=["BOGOTA"])
    assert list(frame["VIAJEROS"]) == [10, 99, 7]


def test_subtopic_filter_keeps_the_original_index():
    frame = charts.travelers_subtopic(_travelers(), "EDAD", [2019], not_known="A. NS/NR")
    assert list(frame.index) == [0, 3]


def test_subtopic_filter_keeps_every_selected_origin():
    frame = charts.travelers_subtopic(_travelers(), "EDAD", [2019], origins=["BOGOTA", "META"])
    assert list(frame["VIAJEROS"]) == [10, 99, 5]


def test_years_of_coerces_to_int():
    assert charts.years_of(["2019", 2020]) == [2019, 2020]


def test_monthly_bar_orders_months_and_labels_ticks():
    frame = charts.by_month_and_item(charts.travelers_subtopic(_travelers(), "EDAD", [2019]))
    fig = charts.monthly_bar(frame, ["#000000"], {"ITEM": ""})
    assert fig.layout.xaxis.tickvals == tuple(charts.MONTHS_ES)
    assert fig.layout.xaxis.ticktext == tuple(charts.MONTHS_EN)
    assert [trace.type for trace in fig.data] == ["bar", "bar"]
    assert fig.layout.xaxis.categoryarray == tuple(charts.MONTHS_ES)


def test_monthly_bar_passes_extra_options():
    fig = charts.monthly_bar(_travelers(), ["#000000"], {}, barmode="group")
    assert fig.layout.barmode == "group"


def test_line_by_origin_dashes_each_origin():
    frame = charts.travelers_subtopic(_travelers(), "EDAD", [2019], not_known="A. NS/NR")
    fig = charts.monthly_line_by_origin(frame, ["#000000"], {})
    dashes = {trace.line.dash for trace in fig.data}
    assert len(fig.data) == 2 and len(dashes) == 2


def test_bar_by_origin_uses_patterns():
    fig = charts.monthly_bar_by_origin(_travelers(), ["#000000"], {})
    assert {trace.marker.pattern.shape for trace in fig.data} == {".", "+"}


def test_month_axis_accepts_other_spellings():
    fig = charts.month_axis(charts.monthly_bar(_travelers(), ["#000"], {}), charts.MONTH_NUMBERS)
    assert fig.layout.xaxis.tickvals[0] == "1"


def test_total_by_item_hides_the_legend():
    fig = charts.total_by_item(_travelers(), ["#000000"])
    assert fig.layout.showlegend is False


@pytest.mark.parametrize(
    "wrap, expected_values", [([True, False], (["1"], "a")), ([False, True], ("1", ["a"]))]
)
def test_menu_loader_wraps_values_per_dropdown(monkeypatch, wrap, expected_values):
    import datalayer

    monkeypatch.setattr(datalayer, "kind_from_clicks", lambda n, i: None)
    monkeypatch.setattr(
        datalayer, "options", lambda column, kind: {"AÑO": [1], "MES": ["a"]}[column]
    )
    result = menu_loader(["AÑO", "MES"], wrap)("0", "0")
    assert result[:2] == ([{"label": "1", "value": "1"}], [{"label": "a", "value": "a"}])
    assert result[2:] == expected_values


def test_occupancy_mean_averages_over_every_selected_year():
    import datalayer
    from dashboard.callbacks.indicators import occupancy_mean

    frame = datalayer.indicator("tasa_ocupacion_airbnb")
    # Three years: with two, mean and median coincide.
    years = sorted(frame["AÑO"].unique())[:3]
    fig = occupancy_mean("tasa_ocupacion_airbnb", charts.MONTH_NUMBERS)([str(y) for y in years])
    expected = frame[frame["AÑO"].isin(years)].groupby("MES")["VALOR"].mean()
    assert list(fig.data[0].y) == pytest.approx(list(expected))


def test_listing_mean_by_several_locations_matches_the_data():
    # Not reached by the first-load snapshots, which select a single location.
    import datalayer
    from dashboard.callbacks.indicators import listings_mean_by_location

    frame = datalayer.indicator("airbnb_homeway")
    locations = list(frame["SUBTEMA"].unique()[:3])
    fig = listings_mean_by_location(locations)
    expected = frame[frame["SUBTEMA"].isin(locations)].groupby("SUBTEMA")["VALOR"].mean()
    plotted = {trace.name: float(trace.y[0]) for trace in fig.data}
    assert plotted == pytest.approx(expected.to_dict())


def test_monthly_totals_keep_only_numeric_columns():
    # pandas 3 concatenates text columns in sum() unless numeric_only is set;
    # the charts never read them, but they cost time and memory.
    totals = charts.by_month_and_item(_travelers())
    assert list(totals.columns) == ["MES", "ITEM", "AÑO", "VIAJEROS"]
