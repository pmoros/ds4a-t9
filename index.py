# import dash-core, dash-html, dash io, bootstrap
import os

import dash_core_components as dcc
import dash_html_components as html

# Dash Bootstrap components
import dash_bootstrap_components as dbc

import layouts

#header_height, footer_height = "8rem", "8rem"
header_height, footer_height = "6rem", "6rem"
MAIN_BLUE = "#20284D"

HEADER_STYLE = {
    "height": header_height,
    "padding-bottom": "1rem",
    "background-color": "white",
    "margin-bottom": "1rem",
}

FOOTER_STYLE = {
    "position": "fixed",
    "bottom": 0,
    "left": 0,
    "right": 0,
    "height": footer_height,
    "padding": "1rem 1rem",
    #"padding-bottom": "1rem",
    "background-color": MAIN_BLUE,
}


# Header
header = html.Div([

        dbc.Row(
            dbc.Col(
                html.Span(
                    [
                        html.Img(src="assets/IDT_transparent_logo2.png", className="header-banner"),
                        #html.H1("IDT"),
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
options_navBar = ["Inicio", "viajeros", "indicadores"]
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
            )
            #dbc.NavItem(dbc.NavLink(options_navBar[1], href="/{}".format(options_navBar[1].lower()))),
            #dbc.NavItem(dbc.NavLink(options_navBar[2], href="/{}".format(options_navBar[1].lower()))),            
        ],
        color=MAIN_BLUE,
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
                html.H4(children="Instituto Distrital de Turismo")
            ],
            md={"size": 3, "offset": 1},
        ),
        dbc.Col(
            children=[
                html.Img(
                    src="assets/ds4a-logo_2x.png",
                    width="20%",
                )
            ],
            md={"size": 2, "offset": 6},
            #lg={"size": 6, "offset": 2},
            #xl={"size": 4, "offset": 2},            
        )
  
    ]
  )
], style=FOOTER_STYLE)

# Containers for pages
content = html.Div([dcc.Location(id="url"), html.Div(id="page-content")])
container = dbc.Container([content])


