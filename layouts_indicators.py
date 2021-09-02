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

opt1_card1_label_top = "Total average monthly offer of Airbnb and Homeaway properties in selected years"
opt1_card1_label_bottom = "Comparison of the monthly average offer of Airbnb and Homeaway properties among the selected locations"

#Pass options to the menus ---- Card1
card1_menu_top_year = data.df_airbnb_homeway['AÑO'].unique()
opt1_card_options['opt1-board1-menu-top-year'] = list(map(layouts.create_options_dropdown, card1_menu_top_year))

#Pass options to the menus ---- Card1
card1_menu_bottom_year = data.df_airbnb_homeway['SUBTEMA'].unique()
opt1_card_options['opt1-board1-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card1_menu_bottom_year))

# --------Card 2 ------
opt1_card2_title = "Hotel occupancy rate"
opt1_card2_subtitle = "Find out what is the hotel occupancy rate in the city of Bogotá"

opt1_card2_label_top = "Average hotel occupancy rate in selected years"
opt1_card2_label_bottom = "Comparison of the hotel occupancy rate among the selected years"

#Pass options to the menus ---- Card2
card2_menu_top_year = data.df_tasa_ocupacion_hotelera['AÑO'].unique()
opt1_card_options['opt1-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_top_year))

#Pass options to the menus ---- Card2
card2_menu_bottom_year = data.df_tasa_ocupacion_hotelera['AÑO'].unique()
opt1_card_options['opt1-board2-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card2_menu_bottom_year))

# --------Card 3 ------
opt1_card3_title = "Airbnb occupancy rate"
opt1_card3_subtitle = "Find out what is the occupancy rate of Airbnb properties in the city of Bogotá"

opt1_card3_label_top = "Average Airbnb occupancy rate in selected years"
opt1_card3_label_bottom = "Airbnb occupancy rate comparison among selected years"

#Pass options to the menus ---- Card3
card3_menu_top_year = data.df_tasa_ocupacion_airbnb['AÑO'].unique()
opt1_card_options['opt1-board3-menu-top-year'] = list(map(layouts.create_options_dropdown, card3_menu_top_year))

#Pass options to the menus ---- Card3
card3_menu_bottom_year = data.df_tasa_ocupacion_airbnb['AÑO'].unique()
opt1_card_options['opt1-board3-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card3_menu_bottom_year))

#-------------OPT1 Container--------------
opt1 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner_darker(banner_image, opt1_title_div),

# ------CARD 1---------------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 1 header
                layouts.get_board_header(
                    opt1_card1_title, opt1_card1_subtitle),
                # Board 1 PLOTS
                dbc.Container([
                    #Board 1 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year primer tablero
                            placeholder="Select the year",
                            options=opt1_card_options['opt1-board1-menu-top-year'],
                            value=[opt1_card_options['opt1-board1-menu-top-year'][0]['value']],
                            id="opt1-board1-menu-top-year",
                            multi=True,
                        ),
                        html.P(opt1_card1_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt1-board1-graph-top",
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
                                    # Menu Year primer tablero
                                    placeholder="Select the location",
                                    options=opt1_card_options['opt1-board1-menu-bottom-year'],
                                    value=[opt1_card_options['opt1-board1-menu-bottom-year'][0]['value']],
                                    id="opt1-board1-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                #md={'size': 6, 'offset': 3}
                            ),

                        ],
                        ),
                        html.P(opt1_card1_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt1-board1-graph-bottom",
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
                                    options=opt1_card_options['opt1-board2-menu-bottom-year'],
                                    value=[opt1_card_options['opt1-board2-menu-bottom-year'][0]['value']],
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
                                    options=opt1_card_options['opt1-board3-menu-bottom-year'],
                                    value=[opt1_card_options['opt1-board3-menu-bottom-year'][0]['value']],
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
opt2_card2_title = "Direct international connectivity indicators"
opt2_card2_subtitle = "Get to know important indicators per year about international conectivity"
opt2_card2_label = ""

#Pass options to the menus ---- Card2
card2_menu_year = data.df_conect_internacional['SUBTEMA'].unique()
opt2_card_options['opt2-board2-menu-year'] = list(map(layouts.create_options_dropdown, card2_menu_year))

# --------Card 3 ------
opt2_card3_title = "Outstanding information on international tourism"
opt2_card3_subtitle = "Discover relevant information about international tourism among the years"
opt2_card3_label = ""

#Pass options to the menus ---- Card3
card3_menu_top_year = data.df_turismo_internacional['VARIABLE'].unique()
opt2_card_options['opt2-board3-menu-top-year'] = list(map(layouts.create_options_dropdown, card3_menu_top_year))

#Pass options to the menus ---- Card3
card3_menu_bottom_year = data.df_turismo_internacional2['VARIABLE'].unique()
opt2_card_options['opt2-board3-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card3_menu_bottom_year))

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
                            placeholder="Select the category",
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
                # Board 3 PLOTS
                dbc.Container([
                    #Board 3 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            placeholder="Select the category",
                            options=opt2_card_options['opt2-board3-menu-top-year'],
                            value=opt2_card_options['opt2-board3-menu-top-year'][0]['value'],
                            id="opt2-board3-menu-top-year",
                        ),
                        html.P(opt2_card3_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt2-board3-graph-top",
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
                                    placeholder="Select the category",
                                    options=opt2_card_options['opt2-board3-menu-bottom-year'],
                                    value=opt2_card_options['opt2-board3-menu-bottom-year'][0]['value'],
                                    id="opt2-board3-menu-bottom-year",
                                )
                            ],
                                xs={'size': 12},
                                #md={'size': 6, 'offset': 3}
                            ),

                        ],
                        ),
                        html.P(opt2_card3_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt2-board3-graph-bottom",
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

#Pass figures to the graphs --- Card1
opt3_board1_graph_figure = data.get_indicators_opt3_b1_g1()

# --------Card 2 ------
opt3_card2_title = "Jobs generated by tourism"
opt3_card2_subtitle = "Discover the number of jobs generated by tourism each year in Bogotá city"

opt3_card2_label_top = "Total number of jobs generated by tourism among the years of the selected category"
opt3_card2_label_bottom = "Comparison of the number of jobs generated by tourism among the quarters of the selected years"

#Pass options to the menus ---- Card2
card2_menu_top_year = data.df_gen_empleo_turismo['SUBTEMA'].unique()
opt3_card_options['opt3-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_top_year))

card2_menu_bottom_year = data.df_gen_empleo_turismo2['AÑO'].unique()
opt3_card_options['opt3-board2-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card2_menu_bottom_year))


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
                            html.P(opt3_card1_label, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                figure=opt3_board1_graph_figure,
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
                            placeholder="Select the category",
                            options=opt3_card_options['opt3-board2-menu-top-year'],
                            value=opt3_card_options['opt3-board2-menu-top-year'][0]['value'],
                            id="opt3-board2-menu-top-year",
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
                                    options=opt3_card_options['opt3-board2-menu-bottom-year'],
                                    value=[opt3_card_options['opt3-board2-menu-bottom-year'][0]['value']],
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

# --- Layout OPT4 (INDICATORS) ----------------------------

opt4_title = ["Get to know some ", "SIGHTSEEING",
              "indicators"]

opt4_title_div = html.Div(
    children=[
        html.Span(html.H1(opt4_title[0], className="main-title")),
        html.Span(
            html.H1(opt4_title[1], className="main-title-bold")),
        html.Span(html.H1(opt4_title[2], className="main-title"))
    ],
    style={"marginLeft": "10%", "marginRight": "10%"},
)

# --------------Cards that will be displayed
opt4_card_options = {}


# --------Card 1 ------
opt4_card1_title = "Establishments with sustainable tourism certification"
opt4_card1_subtitle = "Get to know the number of establishments that have sustainable tourism certification"
opt4_card1_label = "Total establishments with sustainable tourism certification in the selected years"

#Pass options to the menus ---- Card1
card1_menu_year = data.df_cert_turismo_sostenible['AÑO'].unique()
opt4_card_options['opt4-board1-menu-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))

# --------Card 2 ------
opt4_card2_title = "Tourism service providers"
opt4_card2_subtitle = "Find out who are the providers of tourist services in Bogotá city"

opt4_card2_label_top = "Tourism service providers"
opt4_card2_label_bottom = "Tourism service providers"

#Pass options to the menus ---- Card2
card2_menu_top_year = data.df_prest_servicios_turisticos1['SUBTEMA'].unique()
opt4_card_options['opt4-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_top_year))

card2_menu_bottom_year = data.df_prest_servicios_turisticos2['SUBTEMA'].unique()
opt4_card_options['opt4-board2-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card2_menu_bottom_year))

# --------Card 3 ------
opt4_card3_title = "Regional Travel & Tourism Competitiveness Index (RTTCI)"
opt4_card3_subtitle = "Get to know the index of tourist competitiveness of the city. This index is made up of several sub-indices. It registers and measures the factors associated with the competitiveness of tourist activity. In other words, it measures the capacity of a destination to enter markets in a sustainable way"
opt4_card3_label = "Comparison of the regional travel and tourism competitiveness indices among the selected years"

#Pass options to the menus ---- Card3
card3_menu_year = data.df_indice_competitividad_turistica['AÑO'].unique()
opt4_card_options['opt4-board3-menu-year'] = list(map(layouts.create_options_dropdown, card3_menu_year))

# --------Card 4 ------
opt4_card4_title = "Tourist pressure index"
opt4_card4_subtitle = "Discover the index of tourist pressure of the city. This index corresponds to the percentage of average travelers in relation to the resident population of a given destination"
opt4_card4_label = "Tourist pressure index"


#Pass figures to the graphs --- Card4
opt4_board4_graph_figure = data.get_indicators_opt4_b4_g1()

#-------------OPT4 Container--------------
opt4 = dbc.Container(
    children=[
        # ---Main banner
        layouts.get_main_banner_darker(banner_image, opt4_title_div),
        # -------CARD 1 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 1 header
                layouts.get_board_header(
                    opt4_card1_title, opt4_card1_subtitle),
                # Board 1 PLOT
                dbc.Container([
                    # Board 1 Plot 1
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year primer tablero
                                id="opt4-board1-menu-year",
                                #Passing possible options
                                options=opt4_card_options["opt4-board1-menu-year"],
                                #Using the first value as default
                                value=[opt4_card_options['opt4-board1-menu-year'][0]['value']],
                                placeholder="Select the year",
                                multi=True,
                            ),
                            html.P(opt4_card1_label, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="opt4-board1-graph",
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
                    opt4_card2_title, opt4_card2_subtitle),
                # Board 2 PLOTS
                dbc.Container([
                    #Board 2 Plot 1 (Top)
                    html.Div([
                        dcc.Dropdown(
                            # Menu Year segundo tablero
                            placeholder="Select the provider",
                            options=opt4_card_options['opt4-board2-menu-top-year'],
                            value=[opt4_card_options['opt4-board2-menu-top-year'][0]['value']],
                            id="opt4-board2-menu-top-year",
                            multi=True,
                        ),
                        html.P(opt4_card2_label_top, className="board-standard-label-graph"),
                        #"my plot "
                        dcc.Graph(
                            id="opt4-board2-graph-top",
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
                                    placeholder="Select the provider",
                                    options=opt4_card_options['opt4-board2-menu-bottom-year'],
                                    value=[opt4_card_options['opt4-board2-menu-bottom-year'][0]['value']],                             
                                    id="opt4-board2-menu-bottom-year",
                                    multi=True,
                                )
                            ],
                                xs={'size': 12},
                                #md={'size': 6, 'offset': 3}
                            ),

                        ],
                        ),
                        html.P(opt4_card2_label_bottom, className="board-standard-label-graph"),
                        dcc.Graph(
                            id="opt4-board2-graph-bottom",
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

# -------CARD 3 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 3 header
                layouts.get_board_header(
                    opt4_card3_title, opt4_card3_subtitle),
                # Board 3 PLOT
                dbc.Container([
                    # Board 3 Plot 1
                        html.Div([
                            dcc.Dropdown(
                                # Menu Year primer tablero
                                id="opt4-board3-menu-year",
                                #Passing possible options
                                options=opt4_card_options["opt4-board3-menu-year"],
                                #Using the first value as default
                                value=[opt4_card_options['opt4-board3-menu-year'][0]['value']],
                                placeholder="Select the year",
                                multi=True,
                            ),
                            html.P(opt4_card3_label, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                id="opt4-board3-graph",
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

  # -------CARD 4 ------
        dbc.Card(
            dbc.CardBody(children=[
                # Card 4 header
                layouts.get_board_header(
                    opt4_card4_title, opt4_card4_subtitle),
                # Board 4 PLOT
                dbc.Container([
                    # Board 4 Plot 1
                        html.Div([
                            html.P(opt4_card4_label, className="board-standard-label-graph"),
                            #"my plot "
                            dcc.Graph(
                                figure=opt4_board4_graph_figure,
                                id="opt4-board4-graph",
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
      
    ]
)
