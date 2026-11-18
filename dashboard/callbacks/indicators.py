"""Indicators page callbacks.

Moved verbatim from app.py; registered in their original order.
"""

import plotly.express as px
from dash.dependencies import Input, Output

import datalayer
from dashboard.theme import (
    COLOR_PALETTE_CONTINUOUS,
    COLOR_PALETTE_DISCRETE,
    MESES_ORDEN,
)


def register(app):
    # -----------PAGES CALLBACKS ---------------------------
    # -----------Indicadores (OPT1 [ACCOMODATION]) -----------------------

    # Indicators-> ACCOMMODATION -> BOARD 1 -> GRAPH 1 (TOP)
    @app.callback(
        Output("opt1-board1-graph-top", "figure"),
        [
            Input("opt1-board1-menu-top-year", "value"),
        ],
    )
    def update_indicators_opt1_b1_g1(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("airbnb_homeway")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]
        df_plot = df_plot.groupby("SUBTEMA").sum().reset_index()

        fig = px.bar(
            df_plot,
            x="SUBTEMA",
            y="VALOR",
            color="SUBTEMA",
            labels={"VALOR": "Value", "SUBTEMA": "Location"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_xaxes(showticklabels=True)  # hide all the xticks
        fig.update_layout(showlegend=False)
        return fig

    # Indicators-> ACCOMMODATION (option 1) -> BOARD 1 -> GRAPH 2 (BOTTOM)
    @app.callback(
        Output("opt1-board1-graph-bottom", "figure"),
        [
            Input("opt1-board1-menu-bottom-year", "value"),
        ],
    )
    def update_indicators_opt1_b1_g2(selected_locations):
        df_plot = datalayer.indicator("airbnb_homeway")
        df_plot = df_plot[df_plot["SUBTEMA"].isin(selected_locations)]
        df_plot = df_plot.groupby("SUBTEMA").mean().reset_index()

        fig = px.bar(
            df_plot,
            x="SUBTEMA",
            y="VALOR",
            color="SUBTEMA",
            labels={"VALOR": "Value", "SUBTEMA": "Location"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_traces(width=0.5)
        fig.update_layout(showlegend=False)
        return fig

    # Indicators-> ACCOMMODATION (option 1) -> BOARD 2 -> GRAPH 1 (TOP)
    @app.callback(
        Output("opt1-board2-graph-top", "figure"),
        [
            Input("opt1-board2-menu-top-year", "value"),
        ],
    )
    def update_indicators_opt1_b2_g1(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("tasa_ocupacion_hotelera")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]
        df_plot = df_plot.groupby("MES").mean().reset_index()
        df_plot["MESNO"] = df_plot["MES"].replace(MESES_ORDEN)
        df_plot = df_plot.sort_values(by=["MESNO"])

        fig = px.line(
            df_plot,
            x="MES",
            y="VALOR",
            labels={"VALOR": "Value (%)", "AÑO": "Year", "MES": "Month"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "Enero",
                    "Febrero",
                    "Marzo",
                    "Abril",
                    "Mayo",
                    "Junio",
                    "Julio",
                    "Agosto",
                    "Septiembre",
                    "Octubre",
                    "Noviembre",
                    "Diciembre",
                ],
                ticktext=[
                    "JAN",
                    "FEB",
                    "MAR",
                    "APR",
                    "MAY",
                    "JUN",
                    "JUL",
                    "AUG",
                    "SEP",
                    "OCT",
                    "NOV",
                    "DEC",
                ],
            )
        )

        return fig

    # Indicators-> ACCOMMODATION (option 1) -> BOARD 2 -> GRAPH 1 (BOTTOM)
    @app.callback(
        Output("opt1-board2-graph-bottom", "figure"),
        [
            Input("opt1-board2-menu-bottom-year", "value"),
        ],
    )
    def update_indicators_opt1_b2_g2(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("tasa_ocupacion_hotelera")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]

        fig = px.line(
            df_plot,
            x="MES",
            y="VALOR",
            color="AÑO",
            line_group="AÑO",
            labels={"VALOR": "Value (%)", "AÑO": "Year", "MES": "Month"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "Enero",
                    "Febrero",
                    "Marzo",
                    "Abril",
                    "Mayo",
                    "Junio",
                    "Julio",
                    "Agosto",
                    "Septiembre",
                    "Octubre",
                    "Noviembre",
                    "Diciembre",
                ],
                ticktext=[
                    "JAN",
                    "FEB",
                    "MAR",
                    "APR",
                    "MAY",
                    "JUN",
                    "JUL",
                    "AUG",
                    "SEP",
                    "OCT",
                    "NOV",
                    "DEC",
                ],
            )
        )

        return fig

    # Indicators-> ACCOMMODATION (option 1) -> BOARD 3 -> GRAPH 1 (TOP)
    @app.callback(
        Output("opt1-board3-graph-top", "figure"),
        [
            Input("opt1-board3-menu-top-year", "value"),
        ],
    )
    def update_indicators_opt1_b3_g1(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("tasa_ocupacion_airbnb")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]
        df_plot = df_plot.groupby("MES").mean().reset_index()
        # print(df_plot)

        fig = px.line(
            df_plot,
            x="MES",
            y="VALOR",
            labels={"VALOR": "Value (%)", "AÑO": "Year", "MES": "Month"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                ticktext=[
                    "JAN",
                    "FEB",
                    "MAR",
                    "APR",
                    "MAY",
                    "JUN",
                    "JUL",
                    "AUG",
                    "SEP",
                    "OCT",
                    "NOV",
                    "DEC",
                ],
            )
        )
        return fig

    # Indicators-> ACCOMMODATION (option 1) -> BOARD 3 -> GRAPH 1 (BOTTOM)
    @app.callback(
        Output("opt1-board3-graph-bottom", "figure"),
        [
            Input("opt1-board3-menu-bottom-year", "value"),
        ],
    )
    def update_indicators_opt1_b3_g2(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("tasa_ocupacion_airbnb")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]

        fig = px.line(
            df_plot,
            x="MES",
            y="VALOR",
            color="AÑO",
            line_group="AÑO",
            labels={"VALOR": "Value (%)", "AÑO": "Year", "MES": "Month"},
            # template='ggplot2',
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        # fig.layout.plot_bgcolor = 'rgb(255,255,255)'
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
                ticktext=[
                    "JAN",
                    "FEB",
                    "MAR",
                    "APR",
                    "MAY",
                    "JUN",
                    "JUL",
                    "AUG",
                    "SEP",
                    "OCT",
                    "NOV",
                    "DEC",
                ],
            )
        )
        return fig

    # -----------Indicadores (OPT2 [CONNECTIVITY]) -----------------------

    # Indicators-> CONNECTIVITY -> BOARD 1 -> GRAPH 1
    @app.callback(
        Output("opt2-board1-graph", "figure"),
        [
            Input("opt2-board1-menu-year", "value"),
        ],
    )
    def update_indicators_opt2_b1_g1(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("bigdata")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]

        fig = px.bar(
            df_plot,
            x="SUBTEMA",
            y="VALOR",
            color="VARIABLE",
            facet_col="AÑO",
            labels={"SUBTEMA": "Country", "AÑO": "Year", "VALOR": "Total"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_layout(legend_title="Category")

        return fig

    # Indicators-> CONNECTIVITY -> BOARD 2 -> GRAPH 1
    @app.callback(
        Output("opt2-board2-graph", "figure"),
        [
            Input("opt2-board2-menu-year", "value"),
        ],
    )
    def update_indicators_opt2_b2_g1(selected_item):
        df_plot = datalayer.indicator("conect_internacional")
        df_plot = df_plot[df_plot["SUBTEMA"] == selected_item]
        variable = df_plot["VARIABLE"].iloc[0]

        fig = px.bar(
            df_plot,
            x="AÑO",
            y="VALOR",
            color="AÑO",
            labels={"VALOR": variable, "AÑO": "Year"},
            color_continuous_scale=COLOR_PALETTE_CONTINUOUS,
        )
        fig.update_layout(legend_title="Continent")

        return fig

    # Indicators-> CONNECTIVITY -> BOARD 3 -> GRAPH 1
    @app.callback(
        Output("opt2-board3-graph-top", "figure"),
        [
            Input("opt2-board3-menu-top-year", "value"),
        ],
    )
    def update_indicators_opt2_b3_g1(selected_item):
        df_plot = datalayer.indicator("turismo_internacional")
        df_plot = df_plot[df_plot["VARIABLE"] == selected_item]
        clase = df_plot["CLASE"].iloc[0]

        fig = px.line(
            df_plot,
            x="AÑO",
            y="VALOR",
            color="SUBTEMA",
            line_group="SUBTEMA",
            labels={"VALOR": clase, "AÑO": "Year"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_layout(legend_title="Continent")

        return fig

    # Indicators-> CONNECTIVITY -> BOARD 3 -> GRAPH 2
    @app.callback(
        Output("opt2-board3-graph-bottom", "figure"),
        [
            Input("opt2-board3-menu-bottom-year", "value"),
        ],
    )
    def update_indicators_opt2_b3_g2(selected_item):
        df_plot = datalayer.indicator("turismo_internacional2")
        df_plot = df_plot[df_plot["VARIABLE"] == selected_item]

        fig = px.area(
            df_plot,
            x="AÑO",
            y="VALOR",
            color="CLASE",
            line_group="CLASE",
            labels={"VALOR": "Value (%)", "AÑO": "Year"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_layout(legend_title="Category")

        return fig

    # -----------Indicadores (OPT3 [ECONOMIC]) -----------------------

    # Indicators-> ECONOMIC -> BOARD 2 -> GRAPH 1
    @app.callback(
        Output("opt3-board2-graph-top", "figure"),
        [
            Input("opt3-board2-menu-top-year", "value"),
        ],
    )
    def update_indicators_opt3_b2_g1(selected_item):
        df_plot = datalayer.indicator("gen_empleo_turismo")
        df_plot = df_plot[df_plot["SUBTEMA"] == selected_item]

        fig = px.line(
            df_plot,
            x="AÑO",
            y="VALOR",
            color="VARIABLE",
            line_group="VARIABLE",
            labels={"VALOR": "Jobs", "AÑO": "Year"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_traces(mode="markers+lines")
        fig.update_layout(legend_title="Category")
        return fig

    # Indicators-> ECONOMIC -> BOARD 2 -> GRAPH 2
    @app.callback(
        Output("opt3-board2-graph-bottom", "figure"),
        [
            Input("opt3-board2-menu-bottom-year", "value"),
        ],
    )
    def update_indicators_opt3_b2_g2(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("gen_empleo_turismo2")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]

        fig = px.line(
            df_plot,
            x="MES",
            y="VALOR",
            color="AÑO",
            line_group="AÑO",
            labels={
                "VALOR": "Jobs",
                "AÑO": "Year",
                "MES": "Quarter",
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_traces(mode="markers+lines")

        return fig

    # -----------Indicadores (OPT4 [SIGHTSEEING]) -----------------------

    # Indicators-> SIGHTSEEING -> BOARD 1 -> GRAPH 1
    @app.callback(
        Output("opt4-board1-graph", "figure"),
        [
            Input("opt4-board1-menu-year", "value"),
        ],
    )
    def update_indicators_opt4_b1_g1(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("cert_turismo_sostenible")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]

        fig = px.bar(
            df_plot,
            x="VARIABLE",
            y="VALOR",
            color="VARIABLE",
            labels={
                "VARIABLE": "Establishment Type",
                "VALOR": "Total",
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_xaxes(showticklabels=False)  # hide all the xticks
        return fig

    # Indicators-> SIGHTSEEING -> BOARD 2 -> GRAPH 1
    @app.callback(
        Output("opt4-board2-graph-top", "figure"),
        [
            Input("opt4-board2-menu-top-year", "value"),
        ],
    )
    def update_indicators_opt4_b2_g1(selected_item):
        df_plot = datalayer.indicator("prest_servicios_turisticos1")
        df_plot = df_plot[df_plot["SUBTEMA"].isin(selected_item)]

        fig = px.line(
            df_plot,
            x="AÑO",
            y="VALOR",
            color="SUBTEMA",
            line_group="SUBTEMA",
            labels={"VALOR": "Total", "AÑO": "Year", "SUBTEMA": "Provider"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )

        return fig

    # Indicators-> SIGHTSEEING -> BOARD 2 -> GRAPH 2
    @app.callback(
        Output("opt4-board2-graph-bottom", "figure"),
        [
            Input("opt4-board2-menu-bottom-year", "value"),
        ],
    )
    def update_indicators_opt4_b2_g2(selected_item):
        df_plot = datalayer.indicator("prest_servicios_turisticos2")
        df_plot = df_plot[df_plot["SUBTEMA"].isin(selected_item)]

        fig = px.line(
            df_plot,
            x="AÑO",
            y="VALOR",
            color="SUBTEMA",
            line_group="SUBTEMA",
            labels={"VALOR": "Total", "AÑO": "Year", "SUBTEMA": "Provider"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )

        return fig

    # Indicators-> SIGHTSEEING -> BOARD 3 -> GRAPH 1
    @app.callback(
        Output("opt4-board3-graph", "figure"),
        [
            Input("opt4-board3-menu-year", "value"),
        ],
    )
    def update_indicators_opt4_b3_g1(selected_year):
        selected_year = [int(x) for x in selected_year]
        df_plot = datalayer.indicator("indice_competitividad_turistica")
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]

        fig = px.bar_polar(
            df_plot,
            r="VALOR",
            theta="VARIABLE",
            color="AÑO",
            template="plotly_white",
            labels={"VALOR": "Indice", "AÑO": "Year", "VARIABLE": "Category"},
            color_continuous_scale=COLOR_PALETTE_CONTINUOUS,
        )

        fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
        fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

        return fig
