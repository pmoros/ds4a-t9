import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap components
import dash_bootstrap_components as dbc

import layouts
import data

# Alternative 1
MAIN_COLOR_SELECTOR = "#6C7BC4"
# Alternative 2
MAIN_COLOR_SELECTOR = "#7484d4"

# Ideal
# MAIN_COLOR_SELECTOR = "#E6F0FF"


# --------Viajeros layouts------------

# --- Layout general
main_selector_choices = ["National Travelers",
                         "International Travelers"]

main_selector_choices_label = "Interact with each of the filters and discover the information of your interest"

main_board_title = "General Information"

travelers_opt1_main_board_labels = ["Total travelers", "Travelers gender", "Origin",
                          "Education level", "Age"]

# --- Layout OPT1
travelers_opt1_title = ["Meet", "THE TRAVELERS",
              "who visit Bogotá city"]

travelers_opt1_banner_image = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-travelers_opt1-main.jpg"


travelers_opt1_title_div = html.Div(
    children=[
        html.Span(html.H1(travelers_opt1_title[0], className="main-title")),
        html.Span(
            html.H1(travelers_opt1_title[1], className="main-title-bold")),
        html.Span(html.H1(travelers_opt1_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

# ---------Common components


def get_main_selector_category():
    multiple_selector = dbc.Container([
        dbc.Row([
                dbc.Col(
                    html.Div([
                        # Botón Nacionales
                        dbc.Button("National travelers",n_clicks_timestamp='0',\
                                   id="viajeros-selector-national", \
                                   className="main-primary-selector-subpage btn-block"),
                    ], style={'textAlign': "center"}),
                    xs={"size": 12},
                    md={"size": 4}
                ),
                dbc.Col(
                    html.Div([
                        # Botón Internacionales
                        dbc.Button("International travelers", n_clicks_timestamp='0',\
                                   id="viajeros-selector-international", \
                                   className="main-primary-selector-subpage btn-block"),
                    ], style={'textAlign': "center"}),
                    xs={"size": 12},
                    md={"size": 4},
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
    ],
        fluid=True,
    )

    return multiple_selector


# ---------Layout OPT1 -------------------
travelers_opt1_main_board_icons = {}
travelers_opt1_main_board_icons['total_travelers'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-board-logo1.png"
travelers_opt1_main_board_icons['travelers_gender_male'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-hombre.png"
travelers_opt1_main_board_icons['travelers_gender_female'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-mujer.png"
travelers_opt1_main_board_icons['travelers_origin'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-origin.png"
travelers_opt1_main_board_icons['travelers_education'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-education.png"
travelers_opt1_main_board_icons['travelers_age'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-age.png"

# --------------Cards that will be displayed

#Card options for the user
travelers_opt1_card_options = {}

# --------Card 1 ------
travelers_opt1_card1_title = "Where do the travelers who visit Bogotá come from?"
travelers_opt1_card1_subtitle = "Get to know the number of travelers that visit Bogotá city by origin"

#Pass options to the menus ---- Card1

#Loading years
card1_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt1_card_options['board1-menu-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))

#Loading months
card1_menu_month = data.df_viajeros['MES'].unique()
travelers_opt1_card_options['board1-menu-month'] = list(map(layouts.create_options_dropdown, card1_menu_month))


# --------Card 2 ------
travelers_opt1_card2_title = "How old are the travelers?"
travelers_opt1_card2_subtitle = "Get to know the number of travelers that visit Bogotá city by age"

travelers_opt1_card2_label_top = "Age distribution of the total number of travelers who visited Bogotá in the selected years"
travelers_opt1_card2_label_bottom = "Comparison of the age distribution of travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card2

#Loading years
card2_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt1_card_options['travelers_opt1-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_year))
travelers_opt1_card_options['travelers_opt1-board2-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card2_menu_year))

#Loading origin
card2_menu_origin = data.df_viajeros['ORIGEN'].unique()
travelers_opt1_card_options['travelers_opt1-board2-bottom-origin'] = list(map(layouts.create_options_dropdown, card2_menu_origin))

#Pass options to the menus ---- Card2
#card2_menu_right_origin = data.df_viajeros

#Loading years
# card1_menu_year = data.df_viajeros_nacional['AÑO'].unique()
# travelers_opt1_card_options['board1-menu-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))
#
# #Loading months
# card1_menu_month = data.df_viajeros['MES'].unique()
# travelers_opt1_card_options['board1-menu-month'] = list(map(layouts.create_options_dropdown, card1_menu_month))



# --------Card 3 ------
travelers_opt1_card3_title = "What is the predominant gender among travelers?"
travelers_opt1_card3_subtitle = "Discover the number of travelers that visit Bogotá city by gender"

travelers_opt1_card3_label_left = "Gender distribution of the total number of travelers who visited Bogotá in the selected years"
travelers_opt1_card3_label_right = "Comparison of the gender of travelers who visited Bogotá according to their origin"

# --------Card 4 ------
travelers_opt1_card4_title = "What is the educational level of the travelers?"
travelers_opt1_card4_subtitle = "Find out the number of travelers that visit Bogotá city according to their educational level"

travelers_opt1_card4_label_top = "Distribution of the educational level of the total number of travelers who visited Bogotá in the selected years"
travelers_opt1_card4_label_bottom = "Comparison of the educational level of travelers who visited Bogotá according to their origin"

# --------Card 5 ------
travelers_opt1_card5_title = "What is the occupation of the travelers?"
travelers_opt1_card5_subtitle = "Get to know the number of travelers that visit Bogota city by occupation"

travelers_opt1_card5_label_top = "Distribution of the occupation of the total number of travelers who visited Bogotá in the selected years"
travelers_opt1_card5_label_bottom = "Comparison of the occupation of travelers who visited Bogotá according to their origin"

opt1 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner(travelers_opt1_banner_image, travelers_opt1_title_div),
        # ---Main buttons
        get_main_selector_category(),
        # ---Main card general info
        html.Div(id="travelers_opt1-main-board-travelers", children=[
            dbc.Card(
                dbc.CardBody(children=[
                    # Card header
                    dbc.Row([
                        dbc.Col(
                            [
                                html.Div([
                                    html.H3(main_board_title, \
                                            className="main-board-title-subpage"),


                                ],
                                ),
                            ],
                            xs={"size": 12},
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div([
                                dcc.Dropdown(
                                    # Menu Year main tablero
                                    placeholder="Year",
                                    id="main-board-menu-year",
                                    multi=True,
                                ),
                            ],
                            ),
                        ],
                            xs={"size": 12},
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div([
                                dcc.Dropdown(
                                    # Menu Year main tablero
                                    placeholder="Month",
                                    id="main-board-menu-month",
                                    multi=True,
                                ),
                            ])
                        ],
                            xs={"size": 12},
                            md={"size": 4},
                        ),
                    ],

                    ),

                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.Div([
                                    html.Img(
                                        src=travelers_opt1_main_board_icons['total_travelers'],
                                        style={
                                            "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                    ),
                                    # This element gotta be reached using a call back with the id to load content
                                    # That text is burned
                                    html.Span(html.P(
                                        "23M", id="main-board-content-cantidad"), className="main-board-content-big"),

                                ],
                                    className="main-board-container-standard-h",
                                    style={'paddingRight': "0.5rem",
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
                                            src=travelers_opt1_main_board_icons['travelers_gender_male'],
                                            style={
                                                "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                        ),

                                        html.Div([
                                            # This element gotta be reached using a call back with the id to load content
                                            # That text is burned
                                            html.P(
                                                "32%", id="main-board-content-genero-hombre", className="main-board-content-big"),
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
                                            src=travelers_opt1_main_board_icons['travelers_gender_female'],
                                            style={
                                                "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                        ),

                                        html.Div([
                                            # This element gotta be reached using a call back with the id to load content
                                            # That text is burned
                                            html.P(
                                                "68%", id="main-board-content-genero-hombre", className="main-board-content-big"),
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
                                html.P(travelers_opt1_main_board_labels[0],
                                       className="main-board-label"),
                                style={'textAlign': "right",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(travelers_opt1_main_board_labels[1],
                                       className="main-board-label"),
                                style={'textAlign': "right",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 12},
                        ),
                    ],

                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.Img(
                                    src=travelers_opt1_main_board_icons['travelers_origin'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("Valle del Cauca", id="main-board-content-origin",
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
                                    src=travelers_opt1_main_board_icons['travelers_education'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("Undergraduate degree", id="main-board-content-education",
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
                                    src=travelers_opt1_main_board_icons['travelers_age'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("18-30 years", id="main-board-content-age",
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
                                html.P(travelers_opt1_main_board_labels[2],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(travelers_opt1_main_board_labels[3],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(travelers_opt1_main_board_labels[4],
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

        # ------- CARD 1 ---------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 1 header
                layouts.get_board_header(
                    travelers_opt1_card1_title, travelers_opt1_card1_subtitle),
                # Card 1 selector (menus)
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year Board 1
                                options=travelers_opt1_card_options['board1-menu-year'],
                                #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                value=[travelers_opt1_card_options['board1-menu-year'][0]['value']],
                                placeholder="Select the year",
                                id="board1-menu-year",
                                multi=True,
                            ),
                        ],
                        )
                    ],
                        xs={'size': 6},
                        md={'size': 4, 'offset': 2}
                    ),
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Month segundo tablero
                                options=travelers_opt1_card_options['board1-menu-month'],
                                value=[travelers_opt1_card_options['board1-menu-month'][0]['value']],
                                placeholder="Select the month",
                                id="board1-menu-month",
                                multi=True,
                            ),
                        ],
                        )
                    ],
                        xs={'size': 6},
                        md={'size': 4}
                    )

                ],
                    align="center",
                ),

                # Board 1 PLOTS
                dbc.Row([
                    # Board 1 Plot Right
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt1-board1-graph-right",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 10, 'offset': 1},

                    )
                ]
                ),

            ]),
            className="mb-3 main-board-subpage",

        ),

        # -------CARD 2 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 2 header
                layouts.get_board_header(
                    travelers_opt1_card2_title, travelers_opt1_card2_subtitle),
                # Board 2 PLOTS
                dbc.Row([
                    # Board 2 Plot Top
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year segundo tablero
                                placeholder="Select the year",
                                options=travelers_opt1_card_options['travelers_opt1-board2-menu-top-year'],
                                value=[travelers_opt1_card_options['travelers_opt1-board2-menu-top-year'][0]['value']],
                                id="travelers_opt1-board2-menu-top-year",
                                multi=True,
                            ),
                            html.P(travelers_opt1_card2_label_top, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt1-board2-graph-top",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    ),
                    # Board 2 Plot Bottom
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        placeholder="Select the year",
                                        options=travelers_opt1_card_options['travelers_opt1-board2-menu-bottom-year'],
                                        value=[travelers_opt1_card_options['travelers_opt1-board2-menu-bottom-year'][0]['value']],
                                        id="travelers_opt1-board2-menu-bottom-year",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                ),
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        placeholder="Select the origin",
                                        options=travelers_opt1_card_options['travelers_opt1-board2-bottom-origin'],
                                        value=[travelers_opt1_card_options['travelers_opt1-board2-bottom-origin'][0]['value']],
                                        id="travelers_opt1-board2-bottom-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(travelers_opt1_card2_label_bottom, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="travelers_opt1-board2-graph-bottom",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    )
                ]
                ),

            ]),
            className="mb-3 main-board-subpage",

        ),

        # ------CARD 3---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 3 header
                layouts.get_board_header(
                    travelers_opt1_card3_title, travelers_opt1_card3_subtitle),
                # Board 3 PLOTS
                dbc.Row([
                    # Board 3 Plot Left
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year segundo tablero
                                placeholder="Select the year",
                                id="travelers_opt1-board3-row1-menu-left-year",
                                multi=True,
                            ),
                            html.P(travelers_opt1_card3_label_left, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt1-board3-row1-graph-left",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    ),
                    # Board 2 Plot Right
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        placeholder="Select the year",
                                        id="travelers_opt1-board3-row1-menu-right-year",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                ),
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        placeholder="Select the origin",
                                        id="travelers_opt1-board3-row1-right-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(travelers_opt1_card3_label_right, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="travelers_opt1-board3-row1-graph-right",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    )
                ]
                ),

            ]),
            className="mb-3 main-board-subpage",

        ),

        # ------CARD 4---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 4 header
                layouts.get_board_header(
                    travelers_opt1_card4_title, travelers_opt1_card4_subtitle),
                # Board 4 PLOTS
                dbc.Container([
                    #Board 4 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the year",
                            id="travelers_opt1-board4-menu-top-year",
                            multi=True,
                        ),
                        html.P(travelers_opt1_card4_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="travelers_opt1-board4-graph-top",
                        )
                    ],
                        # className=""
                    ),
                    #Board 4 Plot 2 (Bottom)
                    html.Div([
                        #"my plot "
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Select the year",
                                    id="travelers_opt1-board4-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            ),
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Select the origin",
                                    id="travelers_opt1-board4-bottom-origin",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            )

                        ],
                        ),
                        html.P(travelers_opt1_card4_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="travelers_opt1-board4-graph-bottom",
                        )
                    ],
                        # className=""
                    )
                ],
                fluid=True,
                ),

            ]),
            className="mb-3 main-board-subpage",
        ),

# ------CARD 5---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 5 header
                layouts.get_board_header(
                    travelers_opt1_card5_title, travelers_opt1_card5_subtitle),
                # Board 5 PLOTS
                dbc.Container([
                    #Board 5 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the year",
                            id="travelers_opt1-board5-menu-top-year",
                            multi=True,
                        ),
                        html.P(travelers_opt1_card5_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="travelers_opt1-board5-graph-top",
                        )
                    ],
                        # className=""
                    ),
                    #Board 5 Plot 2 (Bottom)
                    html.Div([
                        #"my plot "
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Select the year",
                                    id="travelers_opt1-board5-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            ),
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Select the origin",
                                    id="travelers_opt1-board5-bottom-origin",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            )

                        ],
                        ),
                        html.P(travelers_opt1_card5_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="travelers_opt1-board5-graph-bottom",
                        )
                    ],
                        # className=""
                    )
                ],
                fluid=True,
                ),

            ]),
            className="mb-3 main-board-subpage",

        ),



    ],
    fluid=True,
)


# ---------Layout that will be returned to the user-------------------
# --- Layout OPT 2
travelers_opt2_title = ["Get to know", "THE PREFERENCES",
              "of travelers visiting Bogotá city"]

travelers_opt2_banner_image = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-op2-main.jpg"


travelers_opt2_title_div = html.Div(
    children=[
        html.Span(html.H1(travelers_opt2_title[0], className="main-title")),
        html.Span(
            html.H1(travelers_opt2_title[1], className="main-title-bold")),
        html.Span(html.H1(travelers_opt2_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

travelers_opt2_main_board_labels = ["Trip purpose", "Most visited tourist attraction", "Travel group",
                          "Accommodation", "Higher expense"]


travelers_opt2_main_board_icons = {}
travelers_opt2_main_board_icons['purpose'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-sightseeing.png"
travelers_opt2_main_board_icons['most_visited'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-most-visited.png"
travelers_opt2_main_board_icons['travel_group'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-travelgroup.png"
travelers_opt2_main_board_icons['accommodation'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-accommodation.png"
travelers_opt2_main_board_icons['expense'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-expense.png"

# --------------Cards that will be displayed

#Card options for the user
travelers_opt2_card_options = {}

# --------Card 1 ------
travelers_opt2_card1_title = "What is the trip purpose?"
travelers_opt2_card1_subtitle = "Get to learn why travelers visit Bogotá city"

travelers_opt2_card1_label_top = "Trip purpose of the total number of travelers who visited Bogotá in the selected years"
travelers_opt2_card1_label_bottom = "Comparison of the reason for travel of travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card1

#Loading years
card1_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt2_card_options['travelers_opt2-board1-menu-top-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))
travelers_opt2_card_options['travelers_opt2-board1-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))

#Loading origin
card1_menu_origin = data.df_viajeros['ORIGEN'].unique()
travelers_opt2_card_options['travelers_opt2-board1-bottom-origin'] = list(map(layouts.create_options_dropdown, card1_menu_origin))


# --------Card 2 ------
travelers_opt2_card2_title = "What tourist attractions do travelers visit in Bogotá city?"
travelers_opt2_card2_subtitle = "Discover which tourist attractions are the most frequented by travelers"

travelers_opt2_card2_label_top = "Tourist attractions that travelers visited in the selected years"
travelers_opt2_card2_label_bottom = "Comparison of the reason for travel of travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card2

#Loading years
card2_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt2_card_options['travelers_opt2-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_year))
travelers_opt2_card_options['travelers_opt2-board2-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card2_menu_year))

#Loading origin
card2_menu_origin = data.df_viajeros['ORIGEN'].unique()
travelers_opt2_card_options['travelers_opt2-board2-bottom-origin'] = list(map(layouts.create_options_dropdown, card2_menu_origin))


# --------Card 3 ------
travelers_opt2_card3_title = "How do travelers who visit Bogotá spend their money?"
travelers_opt2_card3_subtitle = "Get to know the distribution of travelers' spending"

travelers_opt2_card3_label_top = "Expenditure distribution of the total number of travelers who visited Bogotá in the selected years"
travelers_opt2_card3_label_bottom = "Comparison of the distribution of spending by travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card3

#Loading years
card3_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt2_card_options['travelers_opt2-board3-menu-top-year'] = list(map(layouts.create_options_dropdown, card3_menu_year))
travelers_opt2_card_options['travelers_opt2-board3-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card3_menu_year))
#Loading origin
card3_menu_origin = data.df_viajeros['ORIGEN'].unique()
travelers_opt2_card_options['travelers_opt2-board3-bottom-origin'] = list(map(layouts.create_options_dropdown, card3_menu_origin))

# --------Card 4 ------
travelers_opt2_card4_title = "Who do travelers visit Bogotá with?"
travelers_opt2_card4_subtitle = "Discover how the travel group of travelers visiting Bogotá is made up"

travelers_opt2_card4_label_top = "Travel group of the total number of travelers who visited Bogotá in the selected years"
travelers_opt2_card4_label_bottom = "Comparison of the travel group of travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card4

#Loading years
card4_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt2_card_options['travelers_opt2-board4-menu-top-year'] = list(map(layouts.create_options_dropdown, card4_menu_year))
travelers_opt2_card_options['travelers_opt2-board4-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card4_menu_year))
#Loading origin
card4_menu_origin = data.df_viajeros['ORIGEN'].unique()
travelers_opt2_card_options['travelers_opt2-board4-bottom-origin'] = list(map(layouts.create_options_dropdown, card4_menu_origin))

# --------Card 5 ------
travelers_opt2_card5_title = "Where do travelers stay in Bogotá?"
travelers_opt2_card5_subtitle = "Find out the number of travelers that visit Bogotá city by accommodation type"

travelers_opt2_card5_label_top = "Accommodation places of the total of travelers who visited Bogotá in the selected years"
travelers_opt2_card5_label_bottom = "Comparison of the place of accommodation of travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card5

#Loading years
card5_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt2_card_options['travelers_opt2-board5-menu-top-year'] = list(map(layouts.create_options_dropdown, card5_menu_year))
travelers_opt2_card_options['travelers_opt2-board5-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card5_menu_year))
#Loading origin
card5_menu_origin = data.df_viajeros['ORIGEN'].unique()
travelers_opt2_card_options['travelers_opt2-board5-bottom-origin'] = list(map(layouts.create_options_dropdown, card5_menu_origin))

# --------Card 6 ------
travelers_opt2_card6_title = "How many nights do travelers stay in Bogotá?"
travelers_opt2_card6_subtitle = "Get to know the number of travelers that visit Bogotá city according to their nights spent"

travelers_opt2_card6_label_top = "Number of nights spent by the total number of travelers who visited Bogotá in the selected years"
travelers_opt2_card6_label_bottom = "Comparison of the number of nights spent by travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card6

#Loading years
card6_menu_year = data.df_viajeros['AÑO'].unique()
travelers_opt2_card_options['travelers_opt2-board6-menu-top-year'] = list(map(layouts.create_options_dropdown, card6_menu_year))

# --------Card 7 ------
travelers_opt2_card7_title = "How are travelers transported in Bogotá?"
travelers_opt2_card7_subtitle = "Get to know the number of travelers that visit Bogotá city by transport means"

travelers_opt2_card7_label_left = "Means of transport frequented by the total number of travelers who visited Bogotá in the selected years"
travelers_opt2_card7_label_right = "Comparison of the means of transport most frequented by travelers who visited Bogotá according to their origin"


opt2 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner(travelers_opt2_banner_image, travelers_opt2_title_div),
        # ---Main buttons
        get_main_selector_category(),
        # ---Main card general info
        html.Div(id="travelers_opt1-main-board-travelers", children=[
            dbc.Card(
                dbc.CardBody(children=[
                    # Card header
                    dbc.Row([
                        dbc.Col(
                            [
                                html.Div([
                                    html.H3(main_board_title, \
                                            className="main-board-title-subpage"),


                                ],
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col([
                            html.Div([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Year",
                                    id="main-board-menu-year",
                                    multi=True,
                                ),
                            ],
                            ),
                        ],
                            width=4,

                        ),
                        dbc.Col([
                            html.Div([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Month",
                                    id="main-board-menu-month",
                                    multi=True,
                                ),
                            ])
                        ],
                            width=4,
                        ),
                    ],

                    ),

                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.Div([
                                    html.Img(
                                        src=travelers_opt2_main_board_icons['purpose'],
                                        style={
                                            "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                    ),
                                    # This element gotta be reached using a call back with the id to load content
                                    # That text is burned
                                    html.Div([
                                        html.Span(html.P(
                                            "65%", id="main-board-content-purpose"), className="main-board-content-big"),
                                        # Burned label
                                        html.Span(html.P(
                                            "Sightseeing", className="main-board-subtitle"))

                                    ])

                                ],
                                    style={"display": "flex", "justifyContent": "center",
                                           'borderRight': "4px solid var(--third-color-contrast)"}

                                ),
                            ],

                            )
                        ],
                            style={"marginTop": "3rem"},
                            md={"size": 6},
                        ),
                        dbc.Col([
                                html.Div([
                                    html.Div([
                                        html.Img(
                                            src=travelers_opt2_main_board_icons['most_visited'],
                                            style={
                                                "width": "6rem", "height": "6rem", "marginRight": "1rem"}
                                        ),

                                        html.Div([
                                            # This element gotta be reached using a call back with the id to load content
                                            # That text is burned
                                            html.P(
                                                "32%", id="main-board-content-genero-hombre", className="main-board-content-big"),
                                            # Burnt label
                                            html.P(
                                                "Malls", className="main-board-subtitle")
                                        ],
                                        )
                                    ],
                                        style={"display": "flex",
                                               "justifyContent": "center"}

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
                                html.P(travelers_opt2_main_board_labels[0],
                                       className="main-board-label"),
                                style={'textAlign': "center",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 12},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(travelers_opt2_main_board_labels[1],
                                       className="main-board-label"),
                                style={'textAlign': "center",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 12},
                        ),
                    ],

                    ),
                    dbc.Row([
                        dbc.Col([
                            html.Div([
                                html.Img(
                                    src=travelers_opt2_main_board_icons['travel_group'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("Work and / or study colleagues", id="main-board-content-travelgroup",
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
                                    src=travelers_opt2_main_board_icons['accommodation'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("own holiday home", id="main-board-content-accomodation",
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
                                    src=travelers_opt2_main_board_icons['expense'],
                                    style={"width": "6rem", "height": "6rem",
                                           "marginRight": "1rem"}
                                ),
                                # This element gotta be reached using a call back with the id to load content
                                # That text is burned
                                html.P("Internal transportation", id="main-board-content-expense",
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
                                html.P(travelers_opt2_main_board_labels[2],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(travelers_opt2_main_board_labels[3],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(travelers_opt2_main_board_labels[4],
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

        # ------CARD 1--------------- Trip purpose ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 1 header
                layouts.get_board_header(
                    travelers_opt2_card1_title, travelers_opt2_card1_subtitle),
                # Board 1 PLOTS
                dbc.Container([
                    #Board 1 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            options=travelers_opt2_card_options['travelers_opt2-board1-menu-top-year'],
                            #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                            value=[travelers_opt2_card_options['travelers_opt2-board1-menu-top-year'][0]['value']],
                            placeholder="Select the year",
                            id="travelers_opt2-board1-menu-top-year",
                            multi=True,
                        ),
                        html.P(travelers_opt2_card1_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="travelers_opt2-board1-graph-top",
                        )
                    ],
                        # className=""
                    ),
                    #Board 1 Plot 2 (Bottom)
                    html.Div([
                        #"my plot "
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    options=travelers_opt2_card_options['travelers_opt2-board1-menu-bottom-year'],
                                    #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                    value=[travelers_opt2_card_options['travelers_opt2-board1-menu-bottom-year'][0]['value']],

                                    placeholder="Select the year",
                                    id="travelers_opt2-board1-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            ),
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    options=travelers_opt2_card_options['travelers_opt2-board1-bottom-origin'],
                                    #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                    value=[travelers_opt2_card_options['travelers_opt2-board1-bottom-origin'][0]['value']],
                                    placeholder="Select the origin",
                                    id="travelers_opt2-board1-bottom-origin",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            )

                        ],
                        ),
                        html.P(travelers_opt2_card1_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="travelers_opt2-board1-graph-bottom",
                        )
                    ],
                        # className=""
                    )
                ],
                fluid=True,
                ),

            ]),
            className="mb-3 main-board-subpage",
        ),

        # ------CARD 2--------------- Tourist attractions ---
        dbc.Card(
            dbc.CardBody(children=[
                # Card 2 header
                layouts.get_board_header(
                    travelers_opt2_card2_title, travelers_opt2_card2_subtitle),
                # Board 2 PLOTS
                html.Div([
                    dcc.Dropdown(
                        # Menu Year segundo tablero
                        placeholder="Select the year",
                        id="travelers_opt2-board2-menu-top-year",
                        multi=True,
                    ),
                    html.P(travelers_opt2_card2_label_top, className="board-standard-label-graph"),
                ],
                    # className=""
                ),
                dbc.Container([
                #Board 2 Plot 1 (Top)
                dbc.Row([
                    # Board 2 Plot Left
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt2-board2-graph-left",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 3}

                    ),
                    # Board 2 Plot Right
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt2-board2-graph-right",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 9}

                    )
                ]
                ),
                    #Board 2 Plot 2 (Bottom)
                    html.Div([
                        #"my plot "
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    options=travelers_opt2_card_options['travelers_opt2-board2-menu-bottom-year'],
                                    #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                    value=[travelers_opt2_card_options['travelers_opt2-board2-menu-bottom-year'][0]['value']],
                                    placeholder="Select the year",
                                    id="travelers_opt2-board2-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            ),
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    options=travelers_opt2_card_options['travelers_opt2-board2-bottom-origin'],
                                    #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                    value=[travelers_opt2_card_options['travelers_opt2-board2-bottom-origin'][0]['value']],
                                    placeholder="Select the origin",
                                    id="travelers_opt2-board2-bottom-origin",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            )

                        ],
                        ),
                        html.P(travelers_opt2_card2_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="travelers_opt2-board2-graph-bottom",
                        )
                    ],
                        # className=""
                    )
                ],
                fluid=True,
                ),

            ]),
            className="mb-3 main-board-subpage",
        ),

        # -------CARD 3 ------ Traveler Expenditure -----
        dbc.Card(
            dbc.CardBody(children=[
                # Card 3 header
                layouts.get_board_header(
                    travelers_opt2_card3_title, travelers_opt2_card3_subtitle),
                # Board 3 PLOTS
                dbc.Container([
                    # Board 3 Plot 1 (Top)
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year tercer tablero
                                options=travelers_opt2_card_options['travelers_opt2-board3-menu-top-year'],
                                #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                value=[travelers_opt2_card_options['travelers_opt2-board3-menu-top-year'][0]['value']],
                                placeholder="Select the year",
                                id="travelers_opt2-board3-menu-top-year",
                                multi=True,
                            ),
                            html.P(travelers_opt2_card3_label_top, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt2-board3-graph-top",
                            )
                        ],
                            # className=""
                    ),
                    # Board 3 Plot 2 (Bottom)
                        html.Div([
                            #"my plot "
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year tercer tablero
                                        options=travelers_opt2_card_options['travelers_opt2-board3-menu-bottom-year'],
                                        #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                        value=[travelers_opt2_card_options['travelers_opt2-board3-menu-bottom-year'][0]['value']],
                                        placeholder="Select the year",
                                        id="travelers_opt2-board3-menu-bottom-year",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                ),
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        #options= ,
                                        #value=whatever_options[0]['value']
                                        options=travelers_opt2_card_options['travelers_opt2-board3-bottom-origin'],
                                        #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                        value=[travelers_opt2_card_options['travelers_opt2-board3-bottom-origin'][0]['value']],
                                        placeholder="Select the origin",
                                        id="travelers_opt2-board3-bottom-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(travelers_opt2_card3_label_bottom, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="travelers_opt2-board3-graph-bottom",
                            )
                        ],
                            # className=""
                        )
                    ],
                    fluid=True,
                    ),

            ]),
            className="mb-3 main-board-subpage",
        ),

       # -------CARD 4 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 4 header
                layouts.get_board_header(
                    travelers_opt2_card4_title, travelers_opt2_card4_subtitle),
                # Board 4 PLOTS
                dbc.Container([
                    # Board 4 Plot 1 (Top)
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year cuarto tablero
                                options=travelers_opt2_card_options['travelers_opt2-board4-menu-top-year'],
                                #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                value=[travelers_opt2_card_options['travelers_opt2-board4-menu-top-year'][0]['value']],
                                placeholder="Select the year",
                                id="travelers_opt2-board4-menu-top-year",
                                multi=True,
                            ),
                            html.P(travelers_opt2_card4_label_top, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt2-board4-graph-top",
                            )
                        ],
                            # className=""
                    ),
                    # Board 4 Plot 2 (Bottom)
                        html.Div([
                            #"my plot "
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year cuarto tablero
                                        options=travelers_opt2_card_options['travelers_opt2-board4-menu-bottom-year'],
                                        #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                        value=[travelers_opt2_card_options['travelers_opt2-board4-menu-bottom-year'][0]['value']],
                                        placeholder="Select the year",
                                        id="travelers_opt2-board4-menu-bottom-year",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                ),
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year cuarto tablero
                                        #options= ,
                                        #value=whatever_options[0]['value']
                                        options=travelers_opt2_card_options['travelers_opt2-board4-bottom-origin'],
                                        #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                        value=[travelers_opt2_card_options['travelers_opt2-board4-bottom-origin'][0]['value']],                                     
                                        placeholder="Select the origin",
                                        id="travelers_opt2-board4-bottom-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(travelers_opt2_card4_label_bottom, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="travelers_opt2-board4-graph-bottom",
                            )
                        ],
                            # className=""
                        )
                    ],
                    fluid=True,
                    ),

            ]),
            className="mb-3 main-board-subpage",

        ),

       # -------CARD 5 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 5 header
                layouts.get_board_header(
                    travelers_opt2_card5_title, travelers_opt2_card5_subtitle),
                # Board 5 PLOTS
                dbc.Row([
                    # Board 5 Plot Top
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year quinto tablero
                                options=travelers_opt2_card_options['travelers_opt2-board5-menu-top-year'],
                                #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                value=[travelers_opt2_card_options['travelers_opt2-board5-menu-top-year'][0]['value']],
                                placeholder="Select the year",
                                id="travelers_opt2-board5-menu-top-year",
                                multi=True,
                            ),
                            html.P(travelers_opt2_card5_label_top, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt2-board5-graph-top",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    ),
                    # Board 5 Plot Bottom
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year quinto tablero
                                        options=travelers_opt2_card_options['travelers_opt2-board5-menu-bottom-year'],
                                        #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                        value=[travelers_opt2_card_options['travelers_opt2-board5-menu-bottom-year'][0]['value']],
                                        placeholder="Select the year",
                                        id="travelers_opt2-board5-menu-bottom-year",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                ),
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year quinto tablero
                                        options=travelers_opt2_card_options['travelers_opt2-board5-bottom-origin'],
                                        #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                        value=[travelers_opt2_card_options['travelers_opt2-board5-bottom-origin'][0]['value']], 
                                        placeholder="Select the origin",
                                        id="travelers_opt2-board5-bottom-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(travelers_opt2_card5_label_bottom, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="travelers_opt2-board5-graph-bottom",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    )
                ]
                ),

            ]),
            className="mb-3 main-board-subpage",

        ),

       # -------CARD 6 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 6 header
                layouts.get_board_header(
                    travelers_opt2_card6_title, travelers_opt2_card6_subtitle),
                # Board 6 PLOT
                dbc.Container([
                    # Board 6 Plot Top
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year sexto tablero
                                placeholder="Select the year",
                                options=travelers_opt2_card_options['travelers_opt2-board6-menu-top-year'],
                                #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                                value=[travelers_opt2_card_options['travelers_opt2-board6-menu-top-year'][0]['value']],
                                id="travelers_opt2-board6-menu-top-year",
                                multi=True,
                            ),
                            html.P(travelers_opt2_card6_label_top, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt2-board6-graph-top",
                            )
                        ],
                            # className=""
                        ),
                    ],
                fluid=True,
                ),
            ]
            ),
            className="mb-3 main-board-subpage",
        ),

       # -------CARD 7 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 7 header
                layouts.get_board_header(
                    travelers_opt2_card7_title, travelers_opt2_card7_subtitle),
                # Board 7 PLOTS
                dbc.Row([
                    # Board 7 Plot Left
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year segundo tablero
                                placeholder="Select the year",
                                id="travelers_opt2-board7-row1-menu-left-year",
                                multi=True,
                            ),
                            html.P(travelers_opt2_card7_label_left, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="travelers_opt2-board7-row1-graph-left",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    ),
                    # Board 7 Plot Right
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        placeholder="Select the year",
                                        id="travelers_opt2-board7-row1-menu-right-year",
                                        #multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                ),
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        #options= ,
                                        #value=whatever_options[0]['value']
                                        placeholder="Select the origin",
                                        id="travelers_opt2-board7-row1-menu-right-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(travelers_opt2_card7_label_right, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="travelers_opt2-board7-row1-graph-right",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 12}

                    )
                ]
                ),

            ]),
            className="mb-3 main-board-subpage",

        ),

        ]),


    ],
    fluid=True,
)
