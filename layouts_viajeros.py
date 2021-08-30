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


CURR_CATEGORY = 'BOTH'
# Ideal
# MAIN_COLOR_SELECTOR = "#E6F0FF"


# --------Viajeros layouts------------

# --- Layout general
main_selector_choices = ["National Travelers",
                         "International Travelers", "Both"]

main_selector_choices_label = "Interact with each of the filters and discover the information of your interest"

main_board_title = "General Information"

opt1_main_board_labels = ["Total travelers", "Travelers gender", "Origin",
                          "Education level", "Age"]

# --- Layout OPT1
opt1_title = ["Meet", "THE TRAVELERS",
              "who visit Bogotá city"]

opt1_banner_image = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-opt1-main.jpg"

opt1_main_board_menu1 = [{'label': "2019", 'value': 2019}, {
    'label': "2020", 'value': 2020}]
# This function makes it possible to visualize the options properly
# opt1_main_board_menu1['value'] = list(
#     map(lambda x: dbc.DropdownItem(x), opt1_main_board_menu1['value']))

opt1_main_board_menu2 = [{'label': "Enero", 'value': "enero"}, {
    'label': "Febrero", 'value': "Febrero"}]
# This function makes it possible to visualize the options properly
# opt1_main_board_menu2['value'] = list(
#     map(lambda x: dbc.DropdownItem(x), opt1_main_board_menu2['value']))

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
                    md={"size": 3},
                ),
                dbc.Col(
                    html.Div([
                        # Botón Internacionales
                        dbc.Button("International travelers", n_clicks_timestamp='0',\
                                   id="viajeros-selector-international", \
                                   className="main-primary-selector-subpage btn-block"),
                    ], style={'textAlign': "center"}),
                    xs={"size": 12},
                    md={"size": 3},
                ),
                dbc.Col(
                    html.Div([
                        # Botón Both
                        dbc.Button("Both",n_clicks_timestamp='0',\
                                   id="viajeros-selector-both", \
                                   className="main-primary-selector-subpage btn-block"),
                    ], style={'textAlign': "center"}),
                    xs={"size": 12},
                    md={"size": 3},
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
opt1_main_board_icons = {}
opt1_main_board_icons['total_travelers'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-board-logo1.png"
opt1_main_board_icons['travelers_gender_male'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-hombre.png"
opt1_main_board_icons['travelers_gender_female'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-genero-mujer.png"
opt1_main_board_icons['travelers_origin'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-origin.png"
opt1_main_board_icons['travelers_education'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-education.png"
opt1_main_board_icons['travelers_age'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-age.png"

# --------------Cards that will be displayed

#Card options for the user
opt1_card_options = {}

# --------Card 1 ------
opt1_card1_title = "Where do the travelers who visit Bogotá come from?"
opt1_card1_subtitle = "Get to know the number of travelers that visit Bogotá city by origin"

# --------Card 2 ------
opt1_card2_title = "How old are the travelers?"
opt1_card2_subtitle = "Get to know the number of travelers that visit Bogotá city by age"

opt1_card2_label_left = "Age distribution of the total number of travelers who visited Bogotá in the selected years"
opt1_card2_label_right = "Comparison of the age distribution of travelers who visited Bogotá according to their origin"


#Pass options to the menus ---- Card2
#card2_menu_right_origin = data.df_viajeros


# --------Card 3 ------
opt1_card3_title = "What is the predominant gender among travelers?"
opt1_card3_subtitle = "Discover the number of travelers that visit Bogotá city by gender"

opt1_card3_label_left = "Gender distribution of the total number of travelers who visited Bogotá in the selected years"
opt1_card3_label_right = "Comparison of the gender of travelers who visited Bogotá according to their origin"

# --------Card 4 ------
opt1_card4_title = "What is the educational level of the travelers?"
opt1_card4_subtitle = "Find out the number of travelers that visit Bogotá city according to their educational level"

opt1_card4_label_top = "Distribution of the educational level of the total number of travelers who visited Bogotá in the selected years"
opt1_card4_label_bottom = "Comparison of the educational level of travelers who visited Bogotá according to their origin"

# --------Card 5 ------
opt1_card5_title = "What is the occupation of the travelers?"
opt1_card5_subtitle = "Get to know the number of travelers that visit Bogota city by occupation"

opt1_card5_label_top = "Distribution of the occupation of the total number of travelers who visited Bogotá in the selected years"
opt1_card5_label_bottom = "Comparison of the occupation of travelers who visited Bogotá according to their origin"

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
                                        src=opt1_main_board_icons['total_travelers'],
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
                                            src=opt1_main_board_icons['travelers_gender_male'],
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
                                            src=opt1_main_board_icons['travelers_gender_female'],
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
                                html.P(opt1_main_board_labels[0],
                                       className="main-board-label"),
                                style={'textAlign': "right",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(opt1_main_board_labels[1],
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
                                    src=opt1_main_board_icons['travelers_education'],
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
                                    src=opt1_main_board_icons['travelers_age'],
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
                                html.P(opt1_main_board_labels[2],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(opt1_main_board_labels[3],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(opt1_main_board_labels[3],
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
                    opt1_card1_title, opt1_card1_subtitle),
                # Card 1 selector (menus)
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year Board 1
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
                    # Board 1 Plot Left
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dcc.Graph(
                                id="opt1-board1-graph-left",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 3}

                    ),
                    # Board 1 Plot Right
                    dbc.Col([
                        html.Div([
                            #"my plot "
                            dcc.Graph(
                                id="opt1-board1-graph-right",
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

            ]),
            className="mb-3 main-board-subpage",

        ),

        # -------CARD 2 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 2 header
                layouts.get_board_header(
                    opt1_card2_title, opt1_card2_subtitle),
                # Board 2 PLOTS
                dbc.Row([
                    # Board 2 Plot Left
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year segundo tablero
                                placeholder="Select the year",
                                id="opt1-board2-row1-menu-left-year",
                                multi=True,
                            ),
                            html.P(opt1_card2_label_left, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="opt1-board2-row1-graph-left",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 6}

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
                                        id="opt1-board2-row1-menu-right-year",
                                        #multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                ),
                                dbc.Col([
                                    dcc.Dropdown(
                                        # Menu Year segundo tablero
                                        options=opt1_card_options['opt1-board2-row1-menu-right-origin'],
                                        value=[opt1_card_options['opt1-board2-row1-menu-right-origin'][0]['value']],
                                        placeholder="Select the origin",
                                        id="opt1-board2-row1-menu-right-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(opt1_card2_label_right, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="opt1-board2-row1-graph-right",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 6}

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
                    opt1_card3_title, opt1_card3_subtitle),
                # Board 3 PLOTS
                dbc.Row([
                    # Board 3 Plot Left
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year segundo tablero
                                placeholder="Select the year",
                                id="opt1-board3-row1-menu-left-year",
                                multi=True,
                            ),
                            html.P(opt1_card3_label_left, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="opt1-board3-row1-graph-left",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 6}

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
                                        id="opt1-board3-row1-menu-right-year",
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
                                        id="opt1-board3-row1-right-origin",
                                        multi=True,
                                    )
                                ],
                                    xs={'size': 12},
                                    md={'size': 6}
                                )

                            ],
                            ),
                            html.P(opt1_card3_label_right, className="board-standard-label-graph"),
                            dcc.Graph(
                                id="opt1-board3-row1-graph-right",
                            )
                        ],
                            # className=""
                        )
                    ],
                        xs={'size': 12},
                        md={'size': 6}

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
                    opt1_card4_title, opt1_card4_subtitle),
                # Board 4 PLOTS
                dbc.Container([
                    #Board 4 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the year",
                            id="opt1-board4-menu-top-year",
                            multi=True,
                        ),
                        html.P(opt1_card4_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt1-board4-graph-top",
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
                                    id="opt1-board4-menu-bottom-year",
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
                                    id="opt1-board4-bottom-origin",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            )

                        ],
                        ),
                        html.P(opt1_card4_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt1-board4-graph-bottom",
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
                    opt1_card5_title, opt1_card5_subtitle),
                # Board 5 PLOTS
                dbc.Container([
                    #Board 5 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the year",
                            id="opt1-board5-menu-top-year",
                            multi=True,
                        ),
                        html.P(opt1_card5_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt1-board5-graph-top",
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
                                    id="opt1-board5-menu-bottom-year",
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
                                    id="opt1-board5-bottom-origin",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                md={'size': 6}
                            )

                        ],
                        ),
                        html.P(opt1_card5_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt1-board5-graph-bottom",
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
# --- Layout OPT2
opt2_title = ["Get to know", "THE PREFERENCES",
              "of travelers visiting Bogotá city"]

opt2_banner_image = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-op2-main.jpg"

opt2_main_board_menu1 = [{'label': "2019", 'value': 2019}, {
    'label': "2020", 'value': 2020}]
# This function makes it possible to visualize the value properly
# opt2_main_board_menu1['value'] = list(
#     map(lambda x: dbc.DropdownItem(x), opt2_main_board_menu1['value']))

opt2_main_board_menu2 = [{'label': "Enero", 'value': "enero"}, {
    'label': "Febrero", 'value': "Febrero"}]
# This function makes it possible to visualize the value properly
# opt2_main_board_menu2['value'] = list(
#     map(lambda x: dbc.DropdownItem(x), opt2_main_board_menu2['value']))

opt2_title_div = html.Div(
    children=[
        html.Span(html.H1(opt2_title[0], className="main-title")),
        html.Span(
            html.H1(opt2_title[1], className="main-title-bold")),
        html.Span(html.H1(opt2_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

opt2_main_board_labels = ["Trip purpose", "Most visited tourist attraction", "Travel group",
                          "Accommodation", "Higher expense"]


opt2_main_board_icons = {}
opt2_main_board_icons['purpose'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-sightseeing.png"
opt2_main_board_icons['most_visited'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-most-visited.png"
opt2_main_board_icons['travel_group'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-travelgroup.png"
opt2_main_board_icons['accommodation'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-accommodation.png"
opt2_main_board_icons['expense'] = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/viajeros-main-expense.png"

opt2 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner(opt2_banner_image, opt2_title_div),
        # ---Main buttons
        get_main_selector_category(),
        # ---Main card general info
        html.Div(id="opt1-main-board-travelers", children=[
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
                                        src=opt2_main_board_icons['purpose'],
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
                                            src=opt2_main_board_icons['most_visited'],
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
                                html.P(opt2_main_board_labels[0],
                                       className="main-board-label"),
                                style={'textAlign': "center",
                                       'marginTop': "0.5rem"}
                            )
                        ],
                            md={"size": 6},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(opt2_main_board_labels[1],
                                       className="main-board-label"),
                                style={'textAlign': "center",
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
                                    src=opt2_main_board_icons['travel_group'],
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
                                    src=opt2_main_board_icons['accommodation'],
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
                                    src=opt2_main_board_icons['expense'],
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
                                html.P(opt2_main_board_labels[2],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(opt2_main_board_labels[3],
                                       className="main-board-label"),
                                style={'textAlign': "center"}
                            )
                        ],
                            md={"size": 4},
                        ),
                        dbc.Col([
                            html.Div(
                                html.P(opt2_main_board_labels[4],
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
