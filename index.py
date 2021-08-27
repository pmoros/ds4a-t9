# import dash-core, dash-html, dash io, bootstrap
import os

import dash_core_components as dcc
import dash_html_components as html

# Dash Bootstrap components
import dash_bootstrap_components as dbc

import layouts

#header_height, footer_height = "8rem", "8rem"
header_height, footer_height = "6rem", "6rem"
MAIN_COLOR_CONTRAST = "#20284D"
MAIN_COLOR_BACKGROUND = "white"

HEADER_STYLE = {
    "height": header_height,
    "padding-bottom": "1rem",
    "background-color": MAIN_COLOR_BACKGROUND,
    "margin-bottom": "1rem",
}

FOOTER_STYLE = {
    #"position": "relative",
    #"position": "fixed",
    "bottom": 0,
    #"left": 0,
    #"right": 0,
    "height": footer_height,
    "padding": "1rem 1rem",
    #"padding-bottom": "1rem",
    "background-color": MAIN_COLOR_CONTRAST,
}


# Header
header = html.Div([

        dbc.Row(
            dbc.Col(
                html.Span(
                    [
                        html.Img(src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/header-top-logo-idt.png", className="header-banner"),
                        #html.Img(src="assets/header-top-logo-idt.png", className="header-banner"),
                        #https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/header-top-logo-idt.png
                    ],
                    className="align-top",
                ),                               
                md={"size": 8, "offset": 2},
                lg={"size": 6, "offset": 2},
                xl={"size": 4, "offset": 2},
            )
        )        

    ], 
    style=HEADER_STYLE,    
    className="container-fluid d-none d-sm-block" 
)

# Navbar
options_navBar = ["Inicio", "viajeros", "indicadores", "Modelo", "About Us"]
options_navBar = [option.upper() for option in options_navBar]

options_drop_navBar = {}
options_drop_navBar[options_navBar[1]] = [{"label":"Quienes son los viajeros?", "value":"viajeros/quienes"},\
    {"label":"Cuales son sus preferencias?", "value":"viajeros/preferencias"}]

options_drop_navBar[options_navBar[2]] = [{"label":"Economicos", "value":"indicadores/economicos"},\
    {"label":"Turismo", "value":"indicadores/turismo"}]

navBar = dbc.NavbarSimple(
        id="navbar",
        children=[
            dbc.NavItem(dbc.NavLink(options_navBar[0], href="/")),
            dbc.NavItem(
                dbc.DropdownMenu(
                    label=options_navBar[1],
                    children=[
                        dbc.DropdownMenuItem(html.A(children=[options_drop_navBar[options_navBar[1]][0]["label"]],\
                            href=options_drop_navBar[options_navBar[1]][0]["value"])),
                        dbc.DropdownMenuItem(html.A(children=[options_drop_navBar[options_navBar[1]][1]["label"]],\
                            href=options_drop_navBar[options_navBar[1]][1]["value"])),                        
                    ],
            ),
            ),
            dbc.NavItem(
                dbc.DropdownMenu(
                    label=options_navBar[2],
                    children=[
                        dbc.DropdownMenuItem(html.A(children=[options_drop_navBar[options_navBar[2]][0]["label"]],\
                            href=options_drop_navBar[options_navBar[2]][0]["value"])),
                        dbc.DropdownMenuItem(html.A(children=[options_drop_navBar[options_navBar[2]][1]["label"]],\
                            href=options_drop_navBar[options_navBar[2]][1]["value"])),                        
                    ],
            ),
            ),
            dbc.NavItem(dbc.NavLink(options_navBar[3], href="/".format(options_navBar[3].lower()))),
            dbc.NavItem(dbc.NavLink(options_navBar[4], href="/about-us")),
        ],
        color=MAIN_COLOR_CONTRAST,
        dark=False,
        expand="lg",
        #fluid=True,
        sticky="top",
        className="mr-auto",
    )

# Footer
footer = html.Div([
    dbc.Row(children=[
        dbc.Col(
            children=[
                html.P("Instituto Distrital de Turismo",id="footer-idt")
            ],
            xs={"size": 5, "offset": 1},
            md={"size": 3, "offset": 1},
        )
    ]
  )
], style=FOOTER_STYLE)

# Containers for pages
content = dbc.Container([dcc.Location(id="url"), html.Div(id="page-content")], fluid=True)
container = dbc.Container([content],fluid=True)


