
import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap components
import dash_bootstrap_components as dbc

import layouts

# Alternative 1
MAIN_COLOR_SELECTOR = "#6C7BC4"
# Alternative 2
MAIN_COLOR_SELECTOR = "#7484d4"

# Ideal
# MAIN_COLOR_SELECTOR = "#E6F0FF"


# --------Viajeros layouts------------

# --- Layout general
main_selector_choices = ["National Travelers",
                         "International Travelers", "Both"]

main_selector_choices_label = "Interact with each of the filters and discover the information of your interest"

main_board_title = "General Information"

main_board_labels = ["Total travelers", "Travelers gender", "Origin",
                     "Education level", "Age"]

# --- Layout OPT1
opt1_title = ["Meet", "THE TRAVELERS",
              "who visit Bogotá city"]

opt1_banner_image = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-opt1-main.jpg"

opt1_main_board_menu1 = {'label': 'Año', 'options': [2020, 2019]}
# This function makes it possible to visualize the options properly
opt1_main_board_menu1['options'] = list(
    map(lambda x: dbc.DropdownMenuItem(x), opt1_main_board_menu1['options']))

opt1_main_board_menu2 = {'label': 'Mes', 'options': ["Enero", "Febrero"]}
# This function makes it possible to visualize the options properly
opt1_main_board_menu2['options'] = list(
    map(lambda x: dbc.DropdownMenuItem(x), opt1_main_board_menu2['options']))

opt1_title_div = html.Div(
    children=[
        html.Span(html.H1(opt1_title[0], className="main-title")),
        html.Span(
            html.H1(opt1_title[1], className="main-title-bold")),
        html.Span(html.H1(opt1_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

# ---------Common components


def get_main_selector_category():
    multiple_selector = html.Div([
        dbc.Row([
                dbc.Col(
                    html.Div([
                        # Botón Nacionales
                        dbc.Button(main_selector_choices[0],\
                                   id="viajeros-selector-national", \
                                   className="main-primary-selector-subpage btn-block"),
                    ], style={'textAlign': "center"}),
                    width=3,
                ),
                dbc.Col(
                    html.Div([
                        # Botón Internacionales
                        dbc.Button(main_selector_choices[1],\
                                   id="viajeros-selector-international", \
                                   className="main-primary-selector-subpage btn-block"),
                    ], style={'textAlign': "center"}),
                    width=3,
                ),
                dbc.Col(
                    html.Div([
                        # Botón Ambos
                        dbc.Button(main_selector_choices[2],\
                                   id="viajeros-selector-both", \
                                   className="main-primary-selector-subpage btn-block"),
                    ], style={'textAlign': "center"}),
                    width=3,
                ),
                ],
                justify="center",
                ),

        dbc.Row([
                dbc.Col(
                    # Mensaje bajo los selectores principales
                    html.Div(html.P(main_selector_choices_label), \
                             style={'fontSize': "20px", 'textAlign': "center", "marginBottom": "2.5rem"}),
                ),
                ],
                justify="center",
                )
    ]
    )

    return multiple_selector


# ---------Layout that will be returned to the user-------------------
opt1_main_board_icons = {}
opt1_main_board_icons['total_travelers'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-board-logo1.png"
opt1_main_board_icons['travelers_gender_male'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-hombre.png"
opt1_main_board_icons['travelers_gender_female'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-mujer.png"
opt1_main_board_icons['travelers_origin'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-origin.png"
opt1_main_board_icons['travelers_education'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-education.png"
opt1_main_board_icons['travelers_age'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-age.png"

opt1 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner(opt1_banner_image, opt1_title_div),
        # ---Main buttons
        get_main_selector_category(),
        # ---Main card general info
        html.Div(id="opt1-main-board-travelers", children=[
            dbc.Card(
                dbc.CardBody(children=[
                    dbc.Row([
                        dbc.Col(
                            [
                                html.Div([
                                    html.H3(main_board_title, \
                                            className="main-board-title-subpage"),
                                    dbc.DropdownMenu(
                                        # Menu Año primer tablero
                                        opt1_main_board_menu1["options"], label=opt1_main_board_menu1["label"], color=MAIN_COLOR_SELECTOR, bs_size="lg", className="m-1 board-menu-subpage",\
                                        id="opt1-main-board-menu-año",
                                    ),
                                    dbc.DropdownMenu(
                                        # Menu Mes segundo tablero
                                        opt1_main_board_menu2["options"], label=opt1_main_board_menu2["label"], color=MAIN_COLOR_SELECTOR, bs_size="lg", className="m-1 board-menu-subpage",\
                                        id="opt1-main-board-menu-mes",
                                    ),
                                ],
                                    className="main-board-header",
                                )
                            ],
                            width=12,
                        ),
                    ],

                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.Div([
                                    html.Img(
                                        src=opt1_main_board_icons['total_travelers'],
                                        style={
                                            "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                    ),
                                    # This element gotta be reached using a call back with the id to load content
                                    # That text is burned
                                    html.Span(html.P(
                                        "23M", id="opt1-main-board-content-cantidad"), className="main-board-content-big"),

                                ],
                                    className="main-board-container-standard-h",
                                    style={
                                    'borderRight': "4px solid var(--third-color-contrast)"}
                                ),
                            ],

                            )
                        ],
                            style={"marginTop": "3rem"},
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div([
                                html.Div([
                                    html.Div([
                                        html.Img(
                                            src=opt1_main_board_icons['travelers_gender_male'],
                                            style={
                                                "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                        ),

                                        html.Div([
                                            # This element gotta be reached using a call back with the id to load content
                                            # That text is burned
                                            html.P(
                                                "32%", id="opt1-main-board-content-genero-hombre", className="main-board-content-big"),
                                            # Burnt label
                                            html.P(
                                                "Men", className="main-board-subtitle")
                                        ],
                                        )
                                    ],
                                        style={"display": "flex",
                                               "justifyContent": "center"}

                                    ),
                                    html.Div([
                                        html.Img(
                                            src=opt1_main_board_icons['travelers_gender_female'],
                                            style={
                                                "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                        ),

                                        html.Div([
                                            # This element gotta be reached using a call back with the id to load content
                                            # That text is burned
                                            html.P(
                                                "68%", id="opt1-main-board-content-genero-hombre", className="main-board-content-big"),
                                            # Burnt label
                                            html.P(
                                                "Women", className="main-board-subtitle")
                                        ],
                                        )
                                    ],
                                        className="main-board-container-standard-h",

                                    ),

                                ],
                                    style={"display": "flex",
                                           "justifyContent": "space-around"}
                                ),

                            ],

                            )
                        ],
                            style={"marginTop": "3rem"},
                            md={"size": 6},
                        ),

                    ],
                        justify="center",

                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Div(
                                html.P(main_board_labels[0],
                                       className="main-board-label"),
                                style={'textAlign': "right",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(main_board_labels[1],
                                       className="main-board-label"),
                                style={'textAlign': "right",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 6},
                        ),
                    ],

                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.Img(
                                    src=opt1_main_board_icons['travelers_origin'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("Valle del Cauca", id="opt1-main-board-content-origin",
                                       className="main-board-content-small"),
                            ],
                                className="main-board-container-standard-v",
                                style={
                                'borderRight': "4px solid var(--third-color-contrast)"}
                            ),
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div([
                                html.Img(
                                    src=opt1_main_board_icons['travelers_education'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("Undergraduate degree", id="opt1-main-board-content-education",
                                       className="main-board-content-small"),
                            ],
                                className="main-board-container-standard-v",
                                style={
                                'borderRight': "4px solid var(--third-color-contrast)"}
                            ),
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div([
                                html.Img(
                                    src=opt1_main_board_icons['travelers_age'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("18-30 years", id="opt1-main-board-content-age",
                                       className="main-board-content-small"),
                            ],
                                className="main-board-container-standard-v",
                            ),
                        ],
                            md={"size": 4},
                        ),
                    ],
                        justify="center",
                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Div(
                                html.P(main_board_labels[2],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(main_board_labels[3],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(main_board_labels[3],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                    ],
                    ),


                ]
                ),
                className="mb-3 main-board-subpage",
            ),
        ]),


    ],
    fluid=True,
)
