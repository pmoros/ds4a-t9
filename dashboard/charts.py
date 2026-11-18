"""Figure builders and the frame filters that feed them.

Pure functions: frames and plain values in, plotly figures out. No Dash
imports, so they can be unit-tested without an app. Every builder reproduces
the original figure exactly (the callback snapshots prove it).
"""

import plotly.express as px

import datalayer
from datalayer import TravelerKind

MONTHS_ES = ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO"]
MONTHS_ES += ["AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
MONTHS_ES_TITLE = [m.capitalize() for m in MONTHS_ES]
MONTH_NUMBERS = [str(n) for n in range(1, 13)]
MONTHS_EN = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN"]
MONTHS_EN += ["JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

MONTH_ORDER = {"MES": MONTHS_ES}

# The static indicator figures and the maps use plotly's T10 palette.
T10 = px.colors.qualitative.T10

COUNTRIES_ALPHA3 = {
    "ALEMANIA": "DEU",
    "ARGENTINA": "ARG",
    "BOLIVIA": "BOL",
    "BRASIL": "BRA",
    "CHILE": "CHL",
    "COSTA RICA": "CRI",
    "ECUADOR": "ECU",
    "ESPAÑA": "ESP",
    "ESTADOS UNIDOS": "USA",
    "FRANCIA": "FRA",
    "ITALIA": "ITA",
    "MEXICO": "MEX",
    "PANAMA": "PAN",
    "PERU": "PER",
    "REINO UNIDO": "GBR",
}
EUROPE = {"DEU", "ESP", "FRA", "ITA", "GBR"}
CONTINENTS_ALPHA3 = {
    code: ("Europe" if code in EUROPE else "Americas") for code in COUNTRIES_ALPHA3.values()
}


# --------------------------------------------------------------------------
# Filters
# --------------------------------------------------------------------------


def years_of(selected):
    """Dropdown values arrive as strings or ints; the data uses ints."""
    return [int(x) for x in selected]


def in_years(frame, selected):
    return frame[frame["AÑO"].isin(years_of(selected))]


def travelers_subtopic(frame, subtopic, years, origins=None, not_known=None):
    """Monthly rows of one SUBTEMA for the selected years (and origins).

    Drops the TOTAL month and, when given, the survey's "don't know" item
    (e.g. ``"A. NS/NR"``), as every travelers board does.
    """
    selected = frame.loc[frame["AÑO"].isin(years_of(years))]
    if origins is not None:
        selected = selected.loc[frame["ORIGEN"].isin([str(x) for x in origins])]
    selected = selected.loc[frame["SUBTEMA"] == subtopic]
    selected = selected.drop(index=selected.loc[selected["MES"] == "TOTAL"].index)
    if not_known is not None:
        selected = selected.drop(index=selected.loc[selected["ITEM"] == not_known].index)
    return selected


def by_month_and_item(frame):
    return frame.groupby(["MES", "ITEM"]).sum().reset_index()


# --------------------------------------------------------------------------
# Axis helpers
# --------------------------------------------------------------------------


def month_axis(fig, tickvals=MONTHS_ES):
    """Show months as JAN..DEC whatever spelling the data uses."""
    fig.update_layout(xaxis=dict(tickmode="array", tickvals=tickvals, ticktext=MONTHS_EN))
    return fig


def bar_without_legend(fig, ticks=True):
    fig.update_xaxes(showticklabels=ticks)
    fig.update_layout(showlegend=False)
    return fig


# --------------------------------------------------------------------------
# Travelers figures
# --------------------------------------------------------------------------


def monthly_bar(frame, palette, labels, **options):
    fig = px.bar(
        frame,
        x="MES",
        y="VIAJEROS",
        color="ITEM",
        color_discrete_sequence=palette,
        category_orders=MONTH_ORDER,
        labels=labels,
        **options,
    )
    return month_axis(fig)


def monthly_polar(frame, palette, labels):
    fig = px.bar_polar(
        frame,
        r="VIAJEROS",
        theta="MES",
        color="ITEM",
        barnorm="percent",
        template="plotly_white",
        color_discrete_sequence=palette,
        category_orders=MONTH_ORDER,
        labels=labels,
    )
    return month_axis(fig)


def monthly_line_by_origin(frame, palette, labels):
    fig = px.line(
        frame,
        x="MES",
        y="VIAJEROS",
        color="ITEM",
        line_dash="ORIGEN",
        color_discrete_sequence=palette,
        category_orders=MONTH_ORDER,
        labels=labels,
    )
    return month_axis(fig)


def monthly_bar_by_origin(frame, palette, labels):
    return monthly_bar(
        frame, palette, labels, pattern_shape="ORIGEN", pattern_shape_sequence=[".", "+"]
    )


def total_by_item(frame, palette):
    fig = px.bar(
        frame.groupby("ITEM").sum().reset_index(),
        x="ITEM",
        y="VIAJEROS",
        color="ITEM",
        labels={"VALOR": "Value", "ITEM": "Atraction"},
        color_discrete_sequence=palette,
    )
    return bar_without_legend(fig)


def region_map(kind, years, months):
    """Travelers by origin: Colombian departments or countries of the world."""
    frame = datalayer.travelers(kind)
    frame = in_years(frame, years)
    frame = frame[frame["MES"].isin(months)]
    plot_data = frame.groupby("ORIGEN").sum().reset_index()

    if kind == TravelerKind.NATIONAL:
        return px.choropleth_mapbox(
            plot_data,
            locations="ORIGEN",
            color="VIAJEROS",
            geojson=datalayer.load_geojson(),
            zoom=4.1,
            featureidkey="properties.NOMBRE_DPT",
            mapbox_style="carto-positron",
            center={"lat": 4.824335, "lon": -74.063644},
            color_continuous_scale="Viridis",
            opacity=0.5,
        )

    plot_data["iso_alpha"] = plot_data["ORIGEN"].replace(COUNTRIES_ALPHA3)
    plot_data["Continent"] = plot_data["iso_alpha"].replace(CONTINENTS_ALPHA3)
    return px.scatter_geo(
        plot_data,
        locations="iso_alpha",
        color="Continent",
        hover_name="ORIGEN",
        size="VIAJEROS",
        projection="natural earth",
    )


# --------------------------------------------------------------------------
# Static indicator figures (rendered into the page layouts)
# --------------------------------------------------------------------------


def gdp_share():
    fig = px.line(
        datalayer.indicator("pib"),
        x="AÑO",
        y="VALOR",
        color="CLASE",
        line_group="CLASE",
        category_orders={
            "CLASE": ["Subsector: Alojamiento y comida", "Sector: Alojamiento y comida"]
        },
        labels={"VALOR": "GDP (%)", "AÑO": "Year", "CLASE": ""},
        color_discrete_sequence=T10,
    )
    fig.update_traces(mode="markers+lines")
    return fig


def tourism_pressure():
    return px.line(
        datalayer.indicator("indice_presion_turistica"),
        x="AÑO",
        y="VALOR",
        labels={"VALOR": "Value", "AÑO": "Year"},
        color_discrete_sequence=T10,
    )
