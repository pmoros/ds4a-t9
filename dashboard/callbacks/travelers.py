"""Travelers page callbacks, declared as data and registered by factories.

Every callback takes the two traveler-kind buttons first. The tables below
keep the original registration order, ids and output shapes, which the
callback snapshots pin.
"""

from dash.dependencies import Input, Output

import datalayer
from dashboard import charts
from dashboard.components import create_options_dropdown
from dashboard.theme import COLOR_PALETTE_DISCRETE as PALETTE
from dashboard.theme import COLOR_PALETTE_DISCRETE_2 as PALETTE_2

KIND_INPUTS = [
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
]

# Axis/legend labels used by the boards.
LABELS = {"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": ""}
LABELS_ORIGIN = dict(LABELS, ORIGEN="ORIGIN")
# Legacy quirk kept on purpose: some charts that are not about trip purpose
# (e.g. age) still title their legend "PURPOSE, ORIGIN".
LABELS_PURPOSE = {"VIAJEROS": "TRAVELERS", "MES": "MONTH", "ITEM": "PURPOSE, ORIGIN", "ORIGEN": ""}


def _kind(national_bt, international_bt):
    return datalayer.kind_from_clicks(national_bt, international_bt)


# --------------------------------------------------------------------------
# Factories (one per callback shape; never define callbacks inside a loop)
# --------------------------------------------------------------------------


def menu_loader(columns, wrap):
    """Fill dropdowns: options for each id, then each id's first value.

    ``columns[i]`` is the data column behind dropdown i; ``wrap[i]`` says
    whether its value is a list (multi-select) or a scalar.
    """

    def callback(national_bt, international_bt):
        kind = _kind(national_bt, international_bt)
        options = {
            column: list(map(create_options_dropdown, datalayer.options(column, kind)))
            for column in set(columns)
        }
        menus = [options[column] for column in columns]
        firsts = [menu[0]["value"] for menu in menus]
        values = [[first] if listed else first for first, listed in zip(firsts, wrap)]
        return tuple(menus + values)

    return callback


def top_figure(subtopic, not_known, chart, palette, labels, **options):
    """Selected years, all origins, summed per month and item."""

    def callback(national_bt, international_bt, selected_year):
        frame = datalayer.travelers(_kind(national_bt, international_bt))
        frame = charts.travelers_subtopic(frame, subtopic, selected_year, not_known=not_known)
        return chart(charts.by_month_and_item(frame), palette, labels, **options)

    return callback


def bottom_figure(subtopic, not_known, chart, palette, labels):
    """Selected years and origins, one series per item and origin."""

    def callback(national_bt, international_bt, selected_year, selected_origin):
        frame = datalayer.travelers(_kind(national_bt, international_bt))
        frame = charts.travelers_subtopic(
            frame, subtopic, selected_year, selected_origin, not_known=not_known
        )
        return chart(frame, palette, labels)

    return callback


def attractions_total(national_bt, international_bt, selected_year):
    frame = datalayer.travelers(_kind(national_bt, international_bt))
    frame = frame[frame["SUBTEMA"] == "ATRACTIVOS"]
    return charts.total_by_item(charts.in_years(frame, selected_year), PALETTE)


def region_map(national_bt, international_bt, years, months):
    return charts.region_map(_kind(national_bt, international_bt), years, months)


def travel_card(national_bt, international_bt, selected_year, selected_month):
    kind = _kind(national_bt, international_bt)
    card = datalayer.travel_card(int(selected_year), selected_month, kind)
    gender = card["Travelers gender"]
    return (
        card["Total travelers"],
        gender[0],
        gender[2],
        card["Origin"],
        card["Education level"],
        card["Age"],
    )


def preference_card(national_bt, international_bt, selected_year, selected_month):
    kind = _kind(national_bt, international_bt)
    card = datalayer.preference_card(int(selected_year), selected_month, kind)
    purpose = card["Trip purpose"]
    visited = card["Most visited tourist attraction"]
    return (
        purpose[0],
        purpose[1],
        visited[0],
        visited[1],
        card["Travel group"],
        card["accommodation"],
        card["Higher expense"],
    )


# --------------------------------------------------------------------------
# Declarations
# --------------------------------------------------------------------------


def _menus(ids, columns, wrap):
    outputs = [Output(i, "options") for i in ids] + [Output(i, "value") for i in ids]
    return outputs, [], menu_loader(columns, wrap)


def _board_menus(board, top="menu-top-year", bottom="menu-bottom-year", origin="bottom-origin"):
    ids = ["%s-%s" % (board, top), "%s-%s" % (board, bottom), "%s-%s" % (board, origin)]
    return _menus(ids, ["AÑO", "AÑO", "ORIGEN"], [True, True, True])


def _top(board, *spec, **options):
    return (
        [Output(board + "-graph-top", "figure")],
        [Input(board + "-menu-top-year", "value")],
        top_figure(*spec, **options),
    )


def _bottom(board, *spec):
    return (
        [Output(board + "-graph-bottom", "figure")],
        [Input(board + "-menu-bottom-year", "value"), Input(board + "-bottom-origin", "value")],
        bottom_figure(*spec),
    )


def _single(output, inputs, callback):
    return [output], inputs, callback


def _card(ids, callback):
    return [Output(i, "children") for i in ids], _MAIN_MENUS, callback


WHO, PREFS = "travelers_opt1-board", "travelers_opt2-board"
_MAIN_MENUS = [Input("main-board-menu-year", "value"), Input("main-board-menu-month", "value")]
_BOARD6 = "travelers_opt2-board6-row1-menu-"
BAR, POLAR = charts.monthly_bar, charts.monthly_polar
LINE, BAR_BY_ORIGIN = charts.monthly_line_by_origin, charts.monthly_bar_by_origin

CALLBACKS = [
    _menus(["main-board-menu-year", "main-board-menu-month"], ["AÑO", "MES"], [False, False]),
    _card(
        ["main-board-content-cantidad", "main-board-content-genero-hombre"]
        + ["main-board-content-genero-mujer", "main-board-content-origin"]
        + ["main-board-content-education", "main-board-content-age"],
        travel_card,
    ),
    _card(
        ["main-board-content-purpose-0", "main-board-content-purpose-1"]
        + ["most-visited-content-0", "most-visited-content-1"]
        + ["main-board-content-travelgroup", "main-board-content-accomodation"]
        + ["main-board-content-expense"],
        preference_card,
    ),
    _board_menus(WHO + "2"),
    _board_menus(WHO + "3"),
    _board_menus(WHO + "4"),
    _board_menus(WHO + "5"),
    _menus(["board1-menu-year", "board1-menu-month"], ["AÑO", "MES"], [True, True]),
    _single(
        Output("travelers_opt1-board1-graph-right", "figure"),
        [Input("board1-menu-year", "value"), Input("board1-menu-month", "value")],
        region_map,
    ),
    _top(WHO + "2", "EDAD", "A. NS/NR", BAR, PALETTE, LABELS),
    _bottom(WHO + "2", "EDAD", "A. NS/NR", LINE, PALETTE, LABELS_PURPOSE),
    _top(WHO + "3", "GENERO", "C. NS/NR", BAR, PALETTE_2, LABELS_ORIGIN, barmode="group"),
    _bottom(WHO + "3", "GENERO", "C. NS/NR", LINE, PALETTE_2, LABELS_ORIGIN),
    _top(WHO + "4", "EDUCACION", "G. NS/NR", BAR, PALETTE, LABELS_ORIGIN),
    _bottom(WHO + "4", "EDUCACION", "G. NS/NR", BAR_BY_ORIGIN, PALETTE, LABELS_ORIGIN),
    _top(WHO + "5", "OCUPACION", "H. NS/NR", BAR, PALETTE, LABELS_ORIGIN),
    _bottom(WHO + "5", "OCUPACION", "H. NS/NR", BAR_BY_ORIGIN, PALETTE, LABELS_ORIGIN),
    _board_menus(PREFS + "3"),
    _board_menus(PREFS + "4"),
    _board_menus(PREFS + "5"),
    # Dead legacy callback: these board-6 "row1" dropdowns exist in no layout
    # (suppress_callback_exceptions hides that). Kept so the callback map and
    # its snapshots stay identical; removing it is a visible change for later.
    _menus(
        [_BOARD6 + "left-year", _BOARD6 + "right-year", _BOARD6 + "right-origin"],
        ["AÑO", "AÑO", "ORIGEN"],
        [True, False, True],
    ),
    _board_menus(PREFS + "7"),
    _board_menus(PREFS + "1"),
    _top(PREFS + "1", "MOTIVO", None, BAR, PALETTE, LABELS),
    _bottom(PREFS + "1", "MOTIVO", None, LINE, PALETTE, LABELS_PURPOSE),
    _board_menus(PREFS + "2"),
    _single(
        Output(PREFS + "2-graph-right", "figure"),
        [Input(PREFS + "2-menu-bottom-year", "value")],
        attractions_total,
    ),
    _bottom(PREFS + "2", "ATRACTIVOS", None, LINE, PALETTE, LABELS_PURPOSE),
    _top(PREFS + "3", "GASTO DISTRI", None, POLAR, PALETTE, LABELS_ORIGIN),
    _bottom(PREFS + "3", "GASTO DISTRI", None, LINE, PALETTE, LABELS_ORIGIN),
    _top(PREFS + "4", "GRUPO", None, BAR, PALETTE, LABELS),
    _bottom(PREFS + "4", "GRUPO", None, LINE, PALETTE, LABELS_ORIGIN),
    _top(PREFS + "5", "ALOJAMIENTO", "G. NS/NR", BAR, PALETTE, LABELS),
    _bottom(PREFS + "5", "ALOJAMIENTO", None, LINE, PALETTE, LABELS_ORIGIN),
    _top(PREFS + "6", "Noches Pernoctadas", None, BAR, PALETTE, LABELS),
    _top(PREFS + "7", "TRANSPORTE", None, BAR, PALETTE, LABELS_ORIGIN),
    _bottom(PREFS + "7", "TRANSPORTE", None, LINE, PALETTE, LABELS_ORIGIN),
]


def register(app):
    for outputs, inputs, callback in CALLBACKS:
        # Outputs go in as separate arguments, as before: a one-element list
        # would turn a single-output callback into a multi-output one.
        app.callback(*outputs, KIND_INPUTS + inputs)(callback)
