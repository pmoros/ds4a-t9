"""Reusable UI pieces: banners, board headers, dropdown options."""

import dash_bootstrap_components as dbc
from dash import html


def get_main_banner_empty(img_url):
    banner = html.Div(
        className="container-fluid main-banner row-full",
        style={"backgroundImage": f"""url("{img_url}")""", "backgroundPosition": "center"},
    )

    return banner


def get_main_banner(img_url, text_div):
    banner = dbc.Row(
        children=[
            dbc.Col(
                html.Div(
                    children=[text_div],
                    className="container-fluid main-banner row-full",
                    style={
                        "backgroundImage": f"""url("{img_url}")""",
                        "backgroundPosition": "center",
                    },
                ),
                width=12,
            ),
        ]
    )

    return banner


def get_main_banner_darker(img_url, text_div):
    banner = dbc.Row(
        children=[
            dbc.Col(
                html.Div(
                    children=[text_div],
                    className="container-fluid main-banner-darker row-full",
                    style={
                        "backgroundImage": f"""url("{img_url}")""",
                        "backgroundPosition": "center",
                    },
                ),
                width=12,
            ),
        ]
    )

    return banner


def get_board_header(title, subtitle):
    my_header = dbc.Container(
        [
            dbc.Row(
                [
                    html.H3(title, className="board-standard-header-title"),
                ],
                justify="center",
            ),
            dbc.Row(
                [
                    html.P(subtitle, className="board-standard-header-subtitle"),
                ],
                justify="center",
            ),
        ],
        fluid=True,
    )

    return my_header


def create_options_dropdown(val):
    """A dcc.Dropdown option whose label and value are both ``str(val)``."""
    text = str(val)
    return {"label": text, "value": text}
