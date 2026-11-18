"""Landing page.

Pages are built on first request and cached (see dashboard.pages).
"""

from functools import cache

import dash_bootstrap_components as dbc
from dash import html


@cache
def _build():
    landingPage_title = ["Welcome", "to the Bogotá tourist information system"]
    landingPage_subtitle = [
        "In this site you will find the main data on the tourist demand of Bogotá"
    ]
    landingPage = dbc.Container(
        children=[
            dbc.Row(
                children=[
                    dbc.Col(
                        html.Div(
                            id="landing-text",
                            children=[
                                html.Div(
                                    id="landing-title",
                                    children=[
                                        html.Span(
                                            html.H1(
                                                landingPage_title[0], className="landing-title-bold"
                                            )
                                        ),
                                        html.Span(
                                            html.H1(landingPage_title[1], className="landing-title")
                                        ),
                                    ],
                                    style={"marginLeft": "10%", "marginRight": "10%"},
                                ),
                                html.Div(
                                    id="landing-subtitle",
                                    children=[
                                        html.Span(
                                            html.P(
                                                landingPage_subtitle[0],
                                                className="landing-subtitle",
                                            )
                                        ),
                                    ],
                                    style={"marginLeft": "10%", "marginRight": "10%"},
                                ),
                            ],
                            # className="container-fluid main-banner row-full",
                            className="container-fluid landing-banner row-full",
                            style={
                                "backgroundImage": """url("https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/landing-image.png")"""
                            },
                            # style={'background-image': '''url("assets/landing-image.png")'''}
                        ),
                        width=12,
                    ),
                ]
            ),
        ],
        fluid=True,
    )

    return {"home": landingPage}


def home():
    return _build()["home"]
