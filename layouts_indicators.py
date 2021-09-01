import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap components
import dash_bootstrap_components as dbc

import data
import layouts



#---- Common elements
banner_image = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/indicators-banner.jpg"

# --- Layout OPT1 (INDICATORS) ----------------------------

opt1_title = ["Get to know some ", "ACCOMMODATION",
              "indicators"]



opt1_title_div = html.Div(
    children=[
        html.Span(html.H1(opt1_title[0], className="main-title")),
        html.Span(
            html.H1(opt1_title[1], className="main-title-bold")),
        html.Span(html.H1(opt1_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

# --------------Cards that will be displayed
opt1_card_options = {}


# --------Card 1 ------
opt1_card1_title = "Average monthly listing of Airbnb & Homeaway properties by location"
opt1_card1_subtitle = "Get to know the average monthly offer of Airbnb and Homeaway properties by location"

opt1_card1_label_left = "Total average monthly offer of Airbnb and Homeaway properties in selected years"
opt1_card1_label_right = "Comparison of the monthly average offer of Airbnb and Homeaway properties among the selected locations"

#Pass options to the menus ---- Card1
card1_menu_left_year = data.df_airbnb_homeway['AÑO'].unique()
opt1_card_options['opt1-board1-row1-menu-left-year'] = list(map(layouts.create_options_dropdown, card1_menu_left_year))

#Pass options to the menus ---- Card1
card1_menu_right_year = data.df_airbnb_homeway['SUBTEMA'].unique()
opt1_card_options['opt1-board1-row1-menu-right-year'] = list(map(layouts.create_options_dropdown, card1_menu_right_year))

# --------Card 2 ------
opt1_card2_title = "Hotel occupancy rate"
opt1_card2_subtitle = "Find out what is the hotel occupancy rate in the city of Bogotá"

opt1_card2_label_top = "Average hotel occupancy rate in selected years"
opt1_card2_label_bottom = "Comparison of the hotel occupancy rate among the selected years"

#Pass options to the menus ---- Card2
card2_menu_top_year = data.df_tasa_ocupacion_hotelera['AÑO'].unique()
opt1_card_options['opt1-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_top_year))

# --------Card 3 ------
opt1_card3_title = "Airbnb occupancy rate"
opt1_card3_subtitle = "Find out what is the occupancy rate of Airbnb properties in the city of Bogotá"

opt1_card3_label_top = "Average Airbnb occupancy rate in selected years"
opt1_card3_label_bottom = "Airbnb occupancy rate comparison among selected years"

#Pass options to the menus ---- Card3
card3_menu_top_year = data.df_tasa_ocupacion_airbnb['AÑO'].unique()
opt1_card_options['opt1-board3-menu-top-year'] = list(map(layouts.create_options_dropdown, card3_menu_top_year))

#-------------OPT1 Container--------------
opt1 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner_darker(banner_image, opt1_title_div),
        # -------CARD 1 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 1 header
                layouts.get_board_header(
                    opt1_card1_title, opt1_card1_subtitle),
                # Board 1 PLOTS
                dbc.Row([
                    # Board 1 Plot Left
                    dbc.Col([
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year segundo tablero
                                #LOADING THE VALUES DIRECTLY !!!!!
                                id="opt1-board1-row1-menu-left-year",
                                #Passing possible options
                                options=opt1_card_options["opt1-board1-row1-menu-left-year"],
                                #Using the first value as default
                                value=opt1_card_options['opt1-board1-row1-menu-left-year'][0]['value'],
                                placeholder="Select the year",
                                multi=True,
                            ),
                            html.P(opt1_card1_label_left, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="opt1-board1-row1-graph-left",
                            ),
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
                                dcc.Dropdown(
                                    # Menu Location
                                    #Passing possible options
                                    options=opt1_card_options["opt1-board1-row1-menu-right-year"],
                                    #Using the first two values as default
                                    value= [opt1_card_options['opt1-board1-row1-menu-right-year'][0]['value'],\
                                        opt1_card_options['opt1-board1-row1-menu-right-year'][1]['value']],
                                    placeholder="Select the location",
                                    id="opt1-board1-row1-menu-right-location",
                                    multi=True,
                                ),
                                html.P(opt1_card1_label_right, className="board-standard-label-graph"),
                                dcc.Graph(
                                    id="opt1-board1-row1-graph-right",
                            )
                        ]
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

# ------CARD 2---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 2 header
                layouts.get_board_header(
                    opt1_card2_title, opt1_card2_subtitle),
                # Board 2 PLOTS
                dbc.Container([
                    #Board 2 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the year",
                            options=opt1_card_options['opt1-board2-menu-top-year'],
                            value=[opt1_card_options['opt1-board2-menu-top-year'][0]['value']],
                            id="opt1-board2-menu-top-year",
                            multi=True,
                        ),
                        html.P(opt1_card2_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt1-board2-graph-top",
                        )
                    ],
                        # className=""
                    ),
                    #Board 2 Plot 2 (Bottom)                  
                    html.Div([
                        #"my plot "
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Select the year",
                                    id="opt1-board2-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                #md={'size': 6, 'offset': 3}
                            ),

                        ],
                        ),
                        html.P(opt1_card2_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt1-board2-graph-bottom",
                        )
                    ],
                        # className=""
                    )                    
                ],
                fluid=True,
                ),

            ]
            ),
            className="mb-3 main-board-subpage",
        ),                

# ------CARD 3---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 3 header
                layouts.get_board_header(
                    opt1_card3_title, opt1_card3_subtitle),
                # Board 3 PLOTS
                dbc.Container([
                    #Board 3 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            placeholder="Select the year",
                            options=opt1_card_options['opt1-board3-menu-top-year'],
                            value=[opt1_card_options['opt1-board3-menu-top-year'][0]['value']],
                            id="opt1-board3-menu-top-year",
                            multi=True,
                        ),
                        html.P(opt1_card3_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt1-board3-graph-top",
                        )
                    ],
                        # className=""
                    ),
                    #Board 3 Plot 2 (Bottom)                  
                    html.Div([
                        #"my plot "
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Select the year",
                                    id="opt1-board3-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                #md={'size': 6, 'offset': 3}
                            ),

                        ],
                        ),
                        html.P(opt1_card3_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt1-board3-graph-bottom",
                        )
                    ],
                        # className=""
                    )                    
                ],
                fluid=True,
                ),

            ]
            ),
            className="mb-3 main-board-subpage",
        ),                



    ]
)

# --- Layout OPT2 (INDICATORS) ----------------------------

opt2_title = ["Get to know some ", "CONNECTIVITY",
              "indicators"]

opt2_title_div = html.Div(
    children=[
        html.Span(html.H1(opt2_title[0], className="main-title")),
        html.Span(
            html.H1(opt2_title[1], className="main-title-bold")),
        html.Span(html.H1(opt2_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

# --------------Cards that will be displayed
opt2_card_options = {}


# --------Card 1 ------
opt2_card1_title = "Flight capacity and flight reservations by travelers country of origin"
opt2_card1_subtitle = "Discover the flight capacity and flight reservations according to the travelers country of origin"
opt2_card1_label = "Distribution of flight capacity and total flight reservations in the selected years"

#Pass options to the menus ---- Card1
card1_menu_year = data.df_bigdata['AÑO'].unique()
opt2_card_options['opt2-board1-menu-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))

# --------Card 2 ------
opt2_card2_title = "Total travelers per year"
opt2_card2_subtitle = "Get to know the total number of travelers who visit the city of Bogotá per year"
opt2_card2_label = "Total travelers per year"

#Pass options to the menus ---- Card2
card2_menu_year = data.df_conect_internacional['SUBTEMA'].unique()
opt2_card_options['opt2-board2-menu-year'] = list(map(layouts.create_options_dropdown, card2_menu_year))

# --------Card 3 ------
opt2_card3_title = "Number of travelers visiting Bogotá by origin"
opt2_card3_subtitle = "Discover the total number of travelers who visit Bogotá city according to their origin"
opt2_card3_label = "Travelers visiting Bogotá by origin"

#Pass options to the menus ---- Card3
card3_menu_year = data.df_turismo_internacional['VARIABLE'].unique()
opt2_card_options['opt2-board3-menu-year'] = list(map(layouts.create_options_dropdown, card3_menu_year))

# --------Card 4 ------
opt2_card4_title = "Number of travelers visiting Bogotá by origin"
opt2_card4_subtitle = "Discover the total number of travelers who visit Bogotá city according to their origin"
opt2_card4_label = "Travelers visiting Bogotá by origin"

#Pass options to the menus ---- Card4
card4_menu_year = data.df_turismo_internacional2['VARIABLE'].unique()
opt2_card_options['opt2-board4-menu-year'] = list(map(layouts.create_options_dropdown, card4_menu_year))

#-------------OPT2 Container--------------
opt2 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner_darker(banner_image, opt2_title_div),
        # -------CARD 1 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 1 header
                layouts.get_board_header(
                    opt2_card1_title, opt2_card1_subtitle),
                # Board 1 PLOT
                dbc.Container([
                    # Board 1 Plot 1
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year primer tablero
                                #LOADING THE VALUES DIRECTLY !!!!!
                                id="opt2-board1-menu-year",
                                #Passing possible options
                                options=opt2_card_options["opt2-board1-menu-year"],
                                #Using the first value as default
                                value=[opt2_card_options['opt2-board1-menu-year'][0]['value']],
                                placeholder="Select the year",
                                multi=True,
                            ),
                            html.P(opt2_card1_label, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="opt2-board1-graph",
                            ),
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

# ------CARD 2---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 2 header
                layouts.get_board_header(
                    opt2_card2_title, opt2_card2_subtitle),
                # Board 2 PLOT
                dbc.Container([
                    #Board 2 Plot 1
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the year",
                            options=opt2_card_options['opt2-board2-menu-year'],
                            value=opt2_card_options['opt2-board2-menu-year'][0]['value'],
                            id="opt2-board2-menu-year"
                        ),
                        html.P(opt2_card2_label, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt2-board2-graph",
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

# ------CARD 3---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 3 header
                layouts.get_board_header(
                    opt2_card3_title, opt2_card3_subtitle),
                # Board 3 PLOT
                dbc.Container([
                    #Board 3 Plot 1
                    html.Div([
                        dcc.Dropdown(
                            placeholder="Select the year",
                            options=opt2_card_options['opt2-board3-menu-year'],
                            value=opt2_card_options['opt2-board3-menu-year'][0]['value'],
                            id="opt2-board3-menu-year"
                        ),
                        html.P(opt2_card3_label, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt2-board3-graph",
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

# ------CARD 4---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 4 header
                layouts.get_board_header(
                    opt2_card4_title, opt2_card4_subtitle),
                # Board 4 PLOT
                dbc.Container([
                    #Board 4 Plot 1
                    html.Div([
                        dcc.Dropdown(
                            placeholder="Select the year",
                            options=opt2_card_options['opt2-board4-menu-year'],
                            value=opt2_card_options['opt2-board4-menu-year'][0]['value'],
                            id="opt2-board4-menu-year",
                        ),
                        html.P(opt2_card4_label, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt2-board4-graph",
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
    ]
)

# --- Layout OPT3 (INDICATORS) ----------------------------

opt3_title = ["Get to know some ", "ECONOMIC",
              "indicators"]

opt3_title_div = html.Div(
    children=[
        html.Span(html.H1(opt3_title[0], className="main-title")),
        html.Span(
            html.H1(opt3_title[1], className="main-title-bold")),
        html.Span(html.H1(opt3_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

# --------------Cards that will be displayed
opt3_card_options = {}


# --------Card 1 ------
opt3_card1_title = "Tourism share in gross domestic product"
opt3_card1_subtitle = "Learn how Bogotá tourism participates in the gross domestic product (GDP). GDP is the monetary value of all goods and services produced by a country in a given period of time"
opt3_card1_label = "Tourism share in gross domestic product"

#Pass options to the menus ---- Card1
#card3_menu_year = data.df_pib['AÑO'].unique()
#opt3_card_options['opt3-board1-menu-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))

# --------Card 2 ------
opt3_card2_title = "Jobs generated by tourism by quarter of the year"
opt3_card2_subtitle = "Discover the number of jobs generated by tourism each quarter of the year in Bogotá city"

opt3_card2_label_top = "Total number of jobs generated by tourism in the quarters of the selected years"
opt3_card2_label_bottom = "Comparison of the number of jobs generated by tourism among the selected years"

#Pass options to the menus ---- Card2
card2_menu_top_year = data.df_gen_empleo_turismo['AÑO'].unique()
opt3_card_options['opt3-board2-menu-top_year'] = list(map(layouts.create_options_dropdown, card2_menu_top_year))

card2_menu_bottom_year = data.df_gen_empleo_turismo['AÑO'].unique()
opt3_card_options['opt3-board2-menu-bottom_year'] = list(map(layouts.create_options_dropdown, card2_menu_bottom_year))


#-------------OPT3 Container--------------
opt3 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner_darker(banner_image, opt3_title_div),
        # -------CARD 1 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 1 header
                layouts.get_board_header(
                    opt3_card1_title, opt3_card1_subtitle),
                # Board 1 PLOT
                dbc.Container([
                    # Board 1 Plot 1
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year primer tablero
                                id="opt3-board1-menu-year",
                                #Passing possible options
                                options=opt3_card_options["opt3-board1-menu-year"],
                                #Using the first value as default
                                value=[opt3_card_options['opt3-board1-menu-year'][0]['value']],
                                placeholder="Select the year",
                                multi=True,
                            ),
                            html.P(opt3_card1_label, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="opt3-board1-graph",
                            ),
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

# ------CARD 2---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 2 header
                layouts.get_board_header(
                    opt3_card2_title, opt3_card2_subtitle),
                # Board 2 PLOTS
                dbc.Container([
                    #Board 2 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the year",
                            options=opt3_card_options['opt3-board2-menu-top-year'],
                            value=[opt3_card_options['opt3-board2-menu-top-year'][0]['value']],
                            id="opt3-board2-menu-top-year",
                            multi=True,
                        ),
                        html.P(opt3_card2_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt3-board2-graph-top",
                        )
                    ],
                        # className=""
                    ),
                    #Board 2 Plot 2 (Bottom)                  
                    html.Div([
                        #"my plot "
                        dbc.Row([
                            dbc.Col([
                                dcc.Dropdown(
                                    # Menu Year segundo tablero
                                    placeholder="Select the year",
                                    id="opt3-board2-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                #md={'size': 6, 'offset': 3}
                            ),

                        ],
                        ),
                        html.P(opt3_card2_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt3-board2-graph-bottom",
                        )
                    ],
                        # className=""
                    )                    
                ],
                fluid=True,
                ),

            ]
            ),
            className="mb-3 main-board-subpage",
        ),                
                   
    ]
)
