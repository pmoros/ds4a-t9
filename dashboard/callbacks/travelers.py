"""Travelers page callbacks.

Moved verbatim from app.py; registered in their original order.
"""

import plotly.express as px
from dash.dependencies import Input, Output

import data
import datalayer
from dashboard.components import create_options_dropdown
from dashboard.theme import (
    COLOR_PALETTE_DISCRETE,
    COLOR_PALETTE_DISCRETE_2,
)
from datalayer import TravelerKind


def register(app):
    # -----------Travelers - Common selectors ----------

    # ----------SELECTOR VALUES LOAD---------------

    # ----------LOAD MAIN CARD--------------
    # Same main card for all OPT, this works for all of them

    @app.callback(
        Output("main-board-menu-year", "options"),
        Output("main-board-menu-month", "options"),
        Output("main-board-menu-year", "value"),
        Output("main-board-menu-month", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_main_board_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_month = datalayer.options("MES", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_month = list(map(create_options_dropdown, menu_month))

        return menu_year, menu_month, menu_year[0]["value"], menu_month[0]["value"]

    # ------------------ CARDS ----------------

    # Travelers -> OPT1 -> MAIN CARD
    @app.callback(
        Output("main-board-content-cantidad", "children"),
        Output("main-board-content-genero-hombre", "children"),
        Output("main-board-content-genero-mujer", "children"),
        Output("main-board-content-origin", "children"),
        Output("main-board-content-education", "children"),
        Output("main-board-content-age", "children"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("main-board-menu-year", "value"),
            Input("main-board-menu-month", "value"),
        ],
    )
    def update_travelers_travel_card(national_bt, international_bt, selected_year, selected_month):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        travel_values = datalayer.travel_card(int(selected_year), selected_month, kind)

        return (
            travel_values["Total travelers"],
            travel_values["Travelers gender"][0],
            travel_values["Travelers gender"][2],
            travel_values["Origin"],
            travel_values["Education level"],
            travel_values["Age"],
        )

    # Travelers -> OPT2 -> MAIN CARD
    @app.callback(
        Output("main-board-content-purpose-0", "children"),
        Output("main-board-content-purpose-1", "children"),
        Output("most-visited-content-0", "children"),
        Output("most-visited-content-1", "children"),
        Output("main-board-content-travelgroup", "children"),
        Output("main-board-content-accomodation", "children"),
        Output("main-board-content-expense", "children"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("main-board-menu-year", "value"),
            Input("main-board-menu-month", "value"),
        ],
    )
    def update_travelers_pref_card(national_bt, international_bt, selected_year, selected_month):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        print("VAL", selected_year)
        print("TYPE", type(selected_year))

        print("VAL", selected_month)
        print("TYPE", type(selected_month))

        pref_values = datalayer.preference_card(int(selected_year), selected_month, kind)

        return (
            pref_values["Trip purpose"][0],
            pref_values["Trip purpose"][1],
            pref_values["Most visited tourist attraction"][0],
            pref_values["Most visited tourist attraction"][1],
            pref_values["Travel group"],
            pref_values["accommodation"],
            pref_values["Higher expense"],
        )

    # -----------Travelers - OPT1 (WHO THEY ARE) -----------------------

    # -----------MENUS LOAD -------------------

    # -----------Load menu OPT1->BOARD2
    @app.callback(
        Output("travelers_opt1-board2-menu-top-year", "options"),
        Output("travelers_opt1-board2-menu-bottom-year", "options"),
        Output("travelers_opt1-board2-bottom-origin", "options"),
        Output("travelers_opt1-board2-menu-top-year", "value"),
        Output("travelers_opt1-board2-menu-bottom-year", "value"),
        Output("travelers_opt1-board2-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt1_board2_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # -----------Load menu OPT1->BOARD3
    @app.callback(
        Output("travelers_opt1-board3-menu-top-year", "options"),
        Output("travelers_opt1-board3-menu-bottom-year", "options"),
        Output("travelers_opt1-board3-bottom-origin", "options"),
        Output("travelers_opt1-board3-menu-top-year", "value"),
        Output("travelers_opt1-board3-menu-bottom-year", "value"),
        Output("travelers_opt1-board3-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt1_board3_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # -----------Load menu OPT1->BOARD4
    @app.callback(
        Output("travelers_opt1-board4-menu-top-year", "options"),
        Output("travelers_opt1-board4-menu-bottom-year", "options"),
        Output("travelers_opt1-board4-bottom-origin", "options"),
        Output("travelers_opt1-board4-menu-top-year", "value"),
        Output("travelers_opt1-board4-menu-bottom-year", "value"),
        Output("travelers_opt1-board4-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt1_board4_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # -----------Load menu OPT1->BOARD5
    @app.callback(
        Output("travelers_opt1-board5-menu-top-year", "options"),
        Output("travelers_opt1-board5-menu-bottom-year", "options"),
        Output("travelers_opt1-board5-bottom-origin", "options"),
        Output("travelers_opt1-board5-menu-top-year", "value"),
        Output("travelers_opt1-board5-menu-bottom-year", "value"),
        Output("travelers_opt1-board5-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt1_board5_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # ----------------MAIN BOARD OPT1 ----------

    # -------------------BOARDS WITHS GRAPHS---------------

    # ------------- BOARD 1 -------------------

    # -----------Load menu OPT1->BOARD1
    @app.callback(
        Output("board1-menu-year", "options"),
        Output("board1-menu-month", "options"),
        Output("board1-menu-year", "value"),
        Output("board1-menu-month", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_board1_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_month = datalayer.options("MES", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_month = list(map(create_options_dropdown, menu_month))

        return menu_year, menu_month, [menu_year[0]["value"]], [menu_month[0]["value"]]

    # Travelers -> OPT1 -> BOARD 1 -> GRAPH

    @app.callback(
        Output("travelers_opt1-board1-graph-right", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("board1-menu-year", "value"),
            Input("board1-menu-month", "value"),
        ],
    )
    def update_travelers_opt1_b1_g2(national_bt, international_bt, years, months):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        if kind == TravelerKind.NATIONAL:
            my_plot = data.viajeros_region_nacional_plot(years, months)
        elif kind == TravelerKind.INTERNATIONAL:
            my_plot = data.viajeros_region_internacional_plot(years, months)

        return my_plot

    # ------------------ BOARD 2 ----------------
    # Travelers -> OPT1 -> BOARD 2 GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt1-board2-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board2-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b2_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[df_plot["SUBTEMA"] == "EDAD"]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "A. NS/NR"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": ""},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT1 -> BOARD 2 GRAPH 2 (BOTTOM)
    @app.callback(
        Output("travelers_opt1-board2-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board2-menu-bottom-year", "value"),
            Input("travelers_opt1-board2-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b2_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "EDAD"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "A. NS/NR"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={
                "VIAJEROS": "TRAVELERS",
                "MES": "MONTH",
                "ITEM": "PURPOSE, ORIGIN",
                "ORIGEN": "",
            },
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 3 ----------------
    # Travelers -> OPT1 -> BOARD 3 GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt1-board3-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board3-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b3_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "GENERO"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "C. NS/NR"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            barmode="group",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE_2,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT1 -> BOARD 3 GRAPH 2 (BOTTOM)
    @app.callback(
        Output("travelers_opt1-board3-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board3-menu-bottom-year", "value"),
            Input("travelers_opt1-board3-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b3_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "GENERO"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "C. NS/NR"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE_2,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 4 ----------------
    # Travelers -> OPT1 -> BOARD 4 GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt1-board4-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board4-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b4_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "EDUCACION"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "G. NS/NR"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT1 -> BOARD 4 GRAPH 2 (BOTTOM)
    @app.callback(
        Output("travelers_opt1-board4-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board4-menu-bottom-year", "value"),
            Input("travelers_opt1-board4-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b4_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "EDUCACION"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "G. NS/NR"].index)

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            pattern_shape="ORIGEN",
            pattern_shape_sequence=[".", "+"],
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 5 ----------------
    # Travelers -> OPT1 -> BOARD 5 GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt1-board5-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board5-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b5_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "OCUPACION"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "H. NS/NR"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT1 -> BOARD 5 GRAPH 2 (BOTTOM)
    @app.callback(
        Output("travelers_opt1-board5-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt1-board5-menu-bottom-year", "value"),
            Input("travelers_opt1-board5-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt1_b5_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "OCUPACION"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "H. NS/NR"].index)

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            pattern_shape="ORIGEN",
            pattern_shape_sequence=[".", "+"],
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # --------------LOAD MENU BOARDS-----------

    # ------------------ BOARD 3 ----------------

    # -----------Load menu OPT2->BOARD3
    @app.callback(
        Output("travelers_opt2-board3-menu-top-year", "options"),
        Output("travelers_opt2-board3-menu-bottom-year", "options"),
        Output("travelers_opt2-board3-bottom-origin", "options"),
        Output("travelers_opt2-board3-menu-top-year", "value"),
        Output("travelers_opt2-board3-menu-bottom-year", "value"),
        Output("travelers_opt2-board3-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt2_board3_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # ------------------ BOARD 4 ----------------

    # -----------Load menu OPT2->BOARD4
    @app.callback(
        Output("travelers_opt2-board4-menu-top-year", "options"),
        Output("travelers_opt2-board4-menu-bottom-year", "options"),
        Output("travelers_opt2-board4-bottom-origin", "options"),
        Output("travelers_opt2-board4-menu-top-year", "value"),
        Output("travelers_opt2-board4-menu-bottom-year", "value"),
        Output("travelers_opt2-board4-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt2_board4_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # ------------------ BOARD 5 ----------------

    # -----------Load menu OPT2->BOARD5
    @app.callback(
        Output("travelers_opt2-board5-menu-top-year", "options"),
        Output("travelers_opt2-board5-menu-bottom-year", "options"),
        Output("travelers_opt2-board5-bottom-origin", "options"),
        Output("travelers_opt2-board5-menu-top-year", "value"),
        Output("travelers_opt2-board5-menu-bottom-year", "value"),
        Output("travelers_opt2-board5-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt2_board5_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # ------------------ BOARD 6 ----------------

    # -----------Load menu OPT2->BOARD6
    @app.callback(
        Output("travelers_opt2-board6-row1-menu-left-year", "options"),
        Output("travelers_opt2-board6-row1-menu-right-year", "options"),
        Output("travelers_opt2-board6-row1-menu-right-origin", "options"),
        Output("travelers_opt2-board6-row1-menu-left-year", "value"),
        Output("travelers_opt2-board6-row1-menu-right-year", "value"),
        Output("travelers_opt2-board6-row1-menu-right-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt2_board6_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            menu_year[0]["value"],
            [menu_origin[0]["value"]],
        )

    # ------------------ BOARD 7 ----------------

    # -----------Load menu OPT2->BOARD7
    @app.callback(
        Output("travelers_opt2-board7-menu-top-year", "options"),
        Output("travelers_opt2-board7-menu-bottom-year", "options"),
        Output("travelers_opt2-board7-bottom-origin", "options"),
        Output("travelers_opt2-board7-menu-top-year", "value"),
        Output("travelers_opt2-board7-menu-bottom-year", "value"),
        Output("travelers_opt2-board7-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt2_board7_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # Travelers -> OPT1 -> BOARD 2 -> MENU -> RIGHT -> ORIGIN

    # -----------Travelers - OPT2 (WHAT THEY PREFER) -----------------------

    # ------------------ BOARD 1 ----------------
    # -----------Load menu OPT2->BOARD1
    @app.callback(
        Output("travelers_opt2-board1-menu-top-year", "options"),
        Output("travelers_opt2-board1-menu-bottom-year", "options"),
        Output("travelers_opt2-board1-bottom-origin", "options"),
        Output("travelers_opt2-board1-menu-top-year", "value"),
        Output("travelers_opt2-board1-menu-bottom-year", "value"),
        Output("travelers_opt2-board1-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt2_board1_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # Travelers -> OPT2 -> BOARD 1 -> trip purpose: GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt2-board1-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board1-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b1_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "MOTIVO"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": ""},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT2 -> BOARD 1 -> trip purpose: GRAPH 2 (BOTTON)
    @app.callback(
        Output("travelers_opt2-board1-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board1-menu-bottom-year", "value"),
            Input("travelers_opt2-board1-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b1_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "MOTIVO"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={
                "VIAJEROS": "TRAVELERS",
                "MES": "MONTH",
                "ITEM": "PURPOSE, ORIGIN",
                "ORIGEN": "",
            },
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 2 ----------------

    # -----------Load menu OPT2->BOARD2
    @app.callback(
        Output("travelers_opt2-board2-menu-top-year", "options"),
        Output("travelers_opt2-board2-menu-bottom-year", "options"),
        Output("travelers_opt2-board2-bottom-origin", "options"),
        Output("travelers_opt2-board2-menu-top-year", "value"),
        Output("travelers_opt2-board2-menu-bottom-year", "value"),
        Output("travelers_opt2-board2-bottom-origin", "value"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
        ],
    )
    def update_travelers_opt2_board1_menu(national_bt, international_bt):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        menu_year = datalayer.options("AÑO", kind)
        menu_origin = datalayer.options("ORIGEN", kind)

        menu_year = list(map(create_options_dropdown, menu_year))
        menu_origin = list(map(create_options_dropdown, menu_origin))

        return (
            menu_year,
            menu_year,
            menu_origin,
            [menu_year[0]["value"]],
            [menu_year[0]["value"]],
            [menu_origin[0]["value"]],
        )

    # Travelers -> OPT2 -> BOARD 2 -> attractions: GRAPH 1 (TOP lEFT)
    @app.callback(
        Output("travelers_opt2-board2-graph-right", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board2-menu-bottom-year", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b2_g3(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)
        df_plot = datalayer.travelers(kind)
        df_plot = df_plot[df_plot["SUBTEMA"] == "ATRACTIVOS"]

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot[df_plot["AÑO"].isin(selected_year)]

        df_plot = df_plot.groupby("ITEM").sum().reset_index()

        fig = px.bar(
            df_plot,
            x="ITEM",
            y="VIAJEROS",
            color="ITEM",
            labels={"VALOR": "Value", "ITEM": "Atraction"},
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
        )
        fig.update_xaxes(showticklabels=True)  # hide all the xticks
        fig.update_layout(showlegend=False)
        return fig

    # Travelers -> OPT2 -> BOARD 2 -> attractions: GRAPH 2 (TOP RIGHT)

    # Travelers -> OPT2 -> BOARD 2 -> attractions: GRAPH 3 (BOTTOM)
    @app.callback(
        Output("travelers_opt2-board2-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board2-menu-bottom-year", "value"),
            Input("travelers_opt2-board2-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b2_g3(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "ATRACTIVOS"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={
                "VIAJEROS": "TRAVELERS",
                "MES": "MONTH",
                "ITEM": "PURPOSE, ORIGIN",
                "ORIGEN": "",
            },
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 3 ----------------

    # Travelers -> OPT2 -> BOARD 3 -> SPENDING: GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt2-board3-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board3-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b3_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        # selected_origin = [str(x) for x in selected_origin]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "GASTO DISTRI"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar_polar(
            df_plot,
            r="VIAJEROS",
            theta="MES",
            color="ITEM",
            barnorm="percent",
            template="plotly_white",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT2 -> BOARD 3 -> SPENDING: GRAPH 2 (BOTTOM)

    @app.callback(
        Output("travelers_opt2-board3-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board3-menu-bottom-year", "value"),
            Input("travelers_opt2-board3-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b3_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "GASTO DISTRI"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 4 ----------------

    # Travelers -> OPT2 -> BOARD 4 -> GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt2-board4-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board4-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b4_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[df_plot["SUBTEMA"] == "GRUPO"]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={
                "VIAJEROS": "TRAVELERS",
                "MES": "MONTH",
                "ITEM": "",
            },
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT2 -> BOARD 4 -> GRAPH 2 (BOTTOM)

    @app.callback(
        Output("travelers_opt2-board4-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board4-menu-bottom-year", "value"),
            Input("travelers_opt2-board4-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b4_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "GRUPO"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 5 ----------------

    # Travelers -> OPT2 -> BOARD 5 -> GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt2-board5-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board5-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b5_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "ALOJAMIENTO"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["ITEM"] == "G. NS/NR"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={
                "VIAJEROS": "TRAVELERS",
                "MES": "MONTH",
                "ITEM": "",
            },
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT2 -> BOARD 5 -> GRAPH 2 (BOTTOM)

    @app.callback(
        Output("travelers_opt2-board5-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board5-menu-bottom-year", "value"),
            Input("travelers_opt2-board5-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b5_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "ALOJAMIENTO"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 6 ----------------

    # Travelers -> OPT2 -> BOARD 6 -> GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt2-board6-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board6-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b6_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "Noches Pernoctadas"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={
                "VIAJEROS": "TRAVELERS",
                "MES": "MONTH",
                "ITEM": "",
            },
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # ------------------ BOARD 7 ----------------

    # Travelers -> OPT2 -> BOARD 7 -> GRAPH 1 (TOP)
    @app.callback(
        Output("travelers_opt2-board7-graph-top", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board7-menu-top-year", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b7_g1(national_bt, international_bt, selected_year):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        df_plot = df_plot.loc[df_plot["AÑO"].isin(selected_year)].loc[
            df_plot["SUBTEMA"] == "TRANSPORTE"
        ]
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)
        df_plot = df_plot.groupby(["MES", "ITEM"]).sum().reset_index()

        fig = px.bar(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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

    # Travelers -> OPT2 -> BOARD 7 -> GRAPH 2 (BOTTOM)

    @app.callback(
        Output("travelers_opt2-board7-graph-bottom", "figure"),
        [
            Input("viajeros-selector-national", "n_clicks_timestamp"),
            Input("viajeros-selector-international", "n_clicks_timestamp"),
            Input("travelers_opt2-board7-menu-bottom-year", "value"),
            Input("travelers_opt2-board7-bottom-origin", "value"),
        ],
    )
    def update_travelers_travelers_opt2_b7_g2(
        national_bt, international_bt, selected_year, selected_origin
    ):
        # USING TYPE OF TOURIST FILTER
        kind = datalayer.kind_from_clicks(national_bt, international_bt)

        # Creating the right graph
        df_plot = datalayer.travelers(kind)

        selected_year = [int(x) for x in selected_year]
        selected_origin = [str(x) for x in selected_origin]

        df_plot = (
            df_plot.loc[df_plot["AÑO"].isin(selected_year)]
            .loc[df_plot["ORIGEN"].isin(selected_origin)]
            .loc[df_plot["SUBTEMA"] == "TRANSPORTE"]
        )
        df_plot = df_plot.drop(index=df_plot.loc[df_plot["MES"] == "TOTAL"].index)

        fig = px.line(
            df_plot,
            x="MES",
            y="VIAJEROS",
            color="ITEM",
            line_dash="ORIGEN",
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            category_orders={
                "MES": [
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
                ]
            },
            labels={"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "", "ORIGEN": "ORIGIN"},
        )
        fig.update_layout(
            xaxis=dict(
                tickmode="array",
                tickvals=[
                    "ENERO",
                    "FEBRERO",
                    "MARZO",
                    "ABRIL",
                    "MAYO",
                    "JUNIO",
                    "JULIO",
                    "AGOSTO",
                    "SEPTIEMBRE",
                    "OCTUBRE",
                    "NOVIEMBRE",
                    "DICIEMBRE",
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
