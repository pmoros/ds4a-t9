"""Indicators page callbacks: one dropdown in, one figure out.

Figures are pure functions of the dropdown value; ``CALLBACKS`` wires each to
its graph and menu, in the original registration order.
"""

import plotly.express as px
from dash.dependencies import Input, Output

import datalayer
from dashboard import charts
from dashboard.theme import COLOR_PALETTE_CONTINUOUS as CONTINUOUS
from dashboard.theme import COLOR_PALETTE_DISCRETE as PALETTE
from dashboard.theme import MESES_ORDEN

OCCUPANCY = {"VALOR": "Value (%)", "AÑO": "Year", "MES": "Month"}
PROVIDERS = {"VALOR": "Total", "AÑO": "Year", "SUBTEMA": "Provider"}
LOCATION = {"VALOR": "Value", "SUBTEMA": "Location"}

# --------------------------------------------------------------------------
# Factories for figures that differ only in their indicator
# --------------------------------------------------------------------------


def occupancy_mean(name, tickvals, sort_months=False):
    """Average occupancy per month over the selected years."""

    def figure(selected_year):
        frame = charts.in_years(datalayer.indicator(name), selected_year)
        frame = frame.groupby("MES").mean().reset_index()
        if sort_months:
            frame["MESNO"] = frame["MES"].replace(MESES_ORDEN)
            frame = frame.sort_values(by=["MESNO"])
        fig = px.line(frame, x="MES", y="VALOR", labels=OCCUPANCY, color_discrete_sequence=PALETTE)
        return charts.month_axis(fig, tickvals)

    return figure


def occupancy_by_year(name, tickvals):
    """Monthly occupancy, one line per selected year."""

    def figure(selected_year):
        fig = px.line(
            charts.in_years(datalayer.indicator(name), selected_year),
            x="MES",
            y="VALOR",
            color="AÑO",
            line_group="AÑO",
            labels=OCCUPANCY,
            color_discrete_sequence=PALETTE,
        )
        return charts.month_axis(fig, tickvals)

    return figure


def providers(name):
    def figure(selected_item):
        frame = datalayer.indicator(name)
        return px.line(
            frame[frame["SUBTEMA"].isin(selected_item)],
            x="AÑO",
            y="VALOR",
            color="SUBTEMA",
            line_group="SUBTEMA",
            labels=PROVIDERS,
            color_discrete_sequence=PALETTE,
        )

    return figure


# --------------------------------------------------------------------------
# One-off figures
# --------------------------------------------------------------------------


def listings_by_location(selected_year):
    frame = charts.in_years(datalayer.indicator("airbnb_homeway"), selected_year)
    frame = frame.groupby("SUBTEMA").sum().reset_index()
    fig = px.bar(
        frame, x="SUBTEMA", y="VALOR", color="SUBTEMA", labels=LOCATION,
        color_discrete_sequence=PALETTE,
    )  # fmt: skip
    return charts.bar_without_legend(fig)


def listings_mean_by_location(selected_locations):
    frame = datalayer.indicator("airbnb_homeway")
    frame = frame[frame["SUBTEMA"].isin(selected_locations)]
    frame = frame.groupby("SUBTEMA").mean().reset_index()
    fig = px.bar(
        frame, x="SUBTEMA", y="VALOR", color="SUBTEMA", labels=LOCATION,
        color_discrete_sequence=PALETTE,
    )  # fmt: skip
    fig.update_traces(width=0.5)
    fig.update_layout(showlegend=False)
    return fig


def flights_by_country(selected_year):
    fig = px.bar(
        charts.in_years(datalayer.indicator("bigdata"), selected_year),
        x="SUBTEMA",
        y="VALOR",
        color="VARIABLE",
        facet_col="AÑO",
        labels={"SUBTEMA": "Country", "AÑO": "Year", "VALOR": "Total"},
        color_discrete_sequence=PALETTE,
    )
    fig.update_layout(legend_title="Category")
    return fig


def international_connectivity(selected_item):
    frame = datalayer.indicator("conect_internacional")
    frame = frame[frame["SUBTEMA"] == selected_item]
    fig = px.bar(
        frame,
        x="AÑO",
        y="VALOR",
        color="AÑO",
        labels={"VALOR": frame["VARIABLE"].iloc[0], "AÑO": "Year"},
        color_continuous_scale=CONTINUOUS,
    )
    fig.update_layout(legend_title="Continent")
    return fig


def international_tourism(selected_item):
    frame = datalayer.indicator("turismo_internacional")
    frame = frame[frame["VARIABLE"] == selected_item]
    fig = px.line(
        frame,
        x="AÑO",
        y="VALOR",
        color="SUBTEMA",
        line_group="SUBTEMA",
        labels={"VALOR": frame["CLASE"].iloc[0], "AÑO": "Year"},
        color_discrete_sequence=PALETTE,
    )
    fig.update_layout(legend_title="Continent")
    return fig


def international_tourism_share(selected_item):
    frame = datalayer.indicator("turismo_internacional2")
    fig = px.area(
        frame[frame["VARIABLE"] == selected_item],
        x="AÑO",
        y="VALOR",
        color="CLASE",
        line_group="CLASE",
        labels={"VALOR": "Value (%)", "AÑO": "Year"},
        color_discrete_sequence=PALETTE,
    )
    fig.update_layout(legend_title="Category")
    return fig


def jobs_by_year(selected_item):
    frame = datalayer.indicator("gen_empleo_turismo")
    fig = px.line(
        frame[frame["SUBTEMA"] == selected_item],
        x="AÑO",
        y="VALOR",
        color="VARIABLE",
        line_group="VARIABLE",
        labels={"VALOR": "Jobs", "AÑO": "Year"},
        color_discrete_sequence=PALETTE,
    )
    fig.update_traces(mode="markers+lines")
    fig.update_layout(legend_title="Category")
    return fig


def jobs_by_quarter(selected_year):
    fig = px.line(
        charts.in_years(datalayer.indicator("gen_empleo_turismo2"), selected_year),
        x="MES",
        y="VALOR",
        color="AÑO",
        line_group="AÑO",
        labels={"VALOR": "Jobs", "AÑO": "Year", "MES": "Quarter"},
        color_discrete_sequence=PALETTE,
    )
    fig.update_traces(mode="markers+lines")
    return fig


def sustainable_certifications(selected_year):
    fig = px.bar(
        charts.in_years(datalayer.indicator("cert_turismo_sostenible"), selected_year),
        x="VARIABLE",
        y="VALOR",
        color="VARIABLE",
        labels={"VARIABLE": "Establishment Type", "VALOR": "Total"},
        color_discrete_sequence=PALETTE,
    )
    fig.update_xaxes(showticklabels=False)
    return fig


def competitiveness(selected_year):
    fig = px.bar_polar(
        charts.in_years(datalayer.indicator("indice_competitividad_turistica"), selected_year),
        r="VALOR",
        theta="VARIABLE",
        color="AÑO",
        template="plotly_white",
        labels={"VALOR": "Indice", "AÑO": "Year", "VARIABLE": "Category"},
        color_continuous_scale=CONTINUOUS,
    )
    framed = dict(showline=True, linewidth=2, linecolor="black", mirror=True)
    fig.update_xaxes(**framed)
    fig.update_yaxes(**framed)
    return fig


# --------------------------------------------------------------------------
# Wiring: (graph id, dropdown id, figure)
# --------------------------------------------------------------------------

CALLBACKS = [
    ("opt1-board1-graph-top", "opt1-board1-menu-top-year", listings_by_location),
    ("opt1-board1-graph-bottom", "opt1-board1-menu-bottom-year", listings_mean_by_location),
    (
        "opt1-board2-graph-top",
        "opt1-board2-menu-top-year",
        occupancy_mean("tasa_ocupacion_hotelera", charts.MONTHS_ES_TITLE, sort_months=True),
    ),
    (
        "opt1-board2-graph-bottom",
        "opt1-board2-menu-bottom-year",
        occupancy_by_year("tasa_ocupacion_hotelera", charts.MONTHS_ES_TITLE),
    ),
    (
        "opt1-board3-graph-top",
        "opt1-board3-menu-top-year",
        occupancy_mean("tasa_ocupacion_airbnb", charts.MONTH_NUMBERS),
    ),
    (
        "opt1-board3-graph-bottom",
        "opt1-board3-menu-bottom-year",
        occupancy_by_year("tasa_ocupacion_airbnb", charts.MONTH_NUMBERS),
    ),
    ("opt2-board1-graph", "opt2-board1-menu-year", flights_by_country),
    ("opt2-board2-graph", "opt2-board2-menu-year", international_connectivity),
    ("opt2-board3-graph-top", "opt2-board3-menu-top-year", international_tourism),
    ("opt2-board3-graph-bottom", "opt2-board3-menu-bottom-year", international_tourism_share),
    ("opt3-board2-graph-top", "opt3-board2-menu-top-year", jobs_by_year),
    ("opt3-board2-graph-bottom", "opt3-board2-menu-bottom-year", jobs_by_quarter),
    ("opt4-board1-graph", "opt4-board1-menu-year", sustainable_certifications),
    (
        "opt4-board2-graph-top",
        "opt4-board2-menu-top-year",
        providers("prest_servicios_turisticos1"),
    ),
    (
        "opt4-board2-graph-bottom",
        "opt4-board2-menu-bottom-year",
        providers("prest_servicios_turisticos2"),
    ),
    ("opt4-board3-graph", "opt4-board3-menu-year", competitiveness),
]


def register(app):
    for graph, menu, figure in CALLBACKS:
        app.callback(Output(graph, "figure"), [Input(menu, "value")])(figure)
