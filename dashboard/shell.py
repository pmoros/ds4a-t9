"""The page frame: header, navigation bar, footer and the page container."""

import dash_bootstrap_components as dbc
from dash import dcc, html

from dashboard.theme import MAIN_COLOR_CONTRAST

# Header
header = html.Div(
    html.Div("", className="header-image"), className="header-banner", id="header-app"
)


# Navbar
options_navBar = ["Home", "Travelers", "Indicators", "About Us"]
options_navBar = [option.upper() for option in options_navBar]

options_drop_navBar = {}
options_drop_navBar[options_navBar[1]] = [
    {"label": "Who are the travelers?", "value": "travelers/who"},
    {"label": "What are their preferences?", "value": "travelers/preferences"},
]

options_drop_navBar[options_navBar[2]] = [
    {"label": "Accommodation", "value": "indicators/accomodation"},
    {"label": "Connectivity", "value": "indicators/connectivity"},
    {"label": "Economic", "value": "indicators/economic"},
    {"label": "Sightseeing", "value": "indicators/sightseeing"},
]

navBar = dbc.NavbarSimple(
    id="navbar",
    children=[
        dbc.NavItem(dbc.NavLink(options_navBar[0], href="/")),
        dbc.NavItem(
            dbc.DropdownMenu(
                label=options_navBar[1],
                children=[
                    dbc.DropdownMenuItem(
                        dbc.NavLink(
                            children=[options_drop_navBar[options_navBar[1]][0]["label"]],
                            href=options_drop_navBar[options_navBar[1]][0]["value"],
                        )
                    ),
                    dbc.DropdownMenuItem(
                        dbc.NavLink(
                            children=[options_drop_navBar[options_navBar[1]][1]["label"]],
                            href=options_drop_navBar[options_navBar[1]][1]["value"],
                        )
                    ),
                ],
            ),
        ),
        dbc.NavItem(
            dbc.DropdownMenu(
                label=options_navBar[2],
                children=[
                    dbc.DropdownMenuItem(
                        dbc.NavLink(
                            children=[options_drop_navBar[options_navBar[2]][0]["label"]],
                            href=options_drop_navBar[options_navBar[2]][0]["value"],
                        )
                    ),
                    # dbc.DropdownMenuItem(dbc.NavLink(options_drop_navBar[options_navBar[2]][0]["label"],\
                    #      href=options_drop_navBar[options_navBar[2]][0]["value"])),
                    dbc.DropdownMenuItem(
                        dbc.NavLink(
                            children=[options_drop_navBar[options_navBar[2]][1]["label"]],
                            href=options_drop_navBar[options_navBar[2]][1]["value"],
                        )
                    ),
                    dbc.DropdownMenuItem(
                        dbc.NavLink(
                            children=[options_drop_navBar[options_navBar[2]][2]["label"]],
                            href=options_drop_navBar[options_navBar[2]][2]["value"],
                        )
                    ),
                    dbc.DropdownMenuItem(
                        dbc.NavLink(
                            children=[options_drop_navBar[options_navBar[2]][3]["label"]],
                            href=options_drop_navBar[options_navBar[2]][3]["value"],
                        )
                    ),
                ],
            ),
        ),
        dbc.NavItem(dbc.NavLink(options_navBar[3], href="/about-us")),
    ],
    color=MAIN_COLOR_CONTRAST,
    dark=False,
    expand="lg",
    # fluid=True,
    sticky="top",
    className="me-auto",
)

# Footer

LOGOS_FOOTER = {}
LOGOS_FOOTER["correlation"] = (
    "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/footer-logo-correlation.png"
)
LOGOS_FOOTER["mintic"] = (
    "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/footer-logo-mintic.png"
)

footer = html.Div(
    [
        html.P(
            "District Tourism Institute of Bogotá",
            className="footer-text-right",
            id="footer-app-text",
        ),
        html.Div(
            [
                html.Img(
                    id="correlation-footer-logo",
                    src=LOGOS_FOOTER["correlation"],
                    style={"width": "153px", "height": "36px"},
                ),
                html.Img(
                    id="mintic-footer-logo",
                    src=LOGOS_FOOTER["mintic"],
                    style={"width": "167px", "height": "100%"},
                ),
            ],
            className="footer-logos-container",
        ),
    ],
    className="footer-container",
    id="footer-app",
)

# Containers for pages
content = dbc.Container([dcc.Location(id="url"), html.Div(id="page-content")], fluid=True)
container = dbc.Container([content], fluid=True, style={"overflow": "hidden"})


def layout():
    return html.Div([header, navBar, container, footer])
