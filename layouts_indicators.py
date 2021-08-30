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

# --------Card 2 ------
opt1_card2_title = "Hotel occupancy rate"
opt1_card2_subtitle = "Find out what is the hotel occupancy rate in the city of Bogotá"

opt1_card2_label_top = "Average hotel occupancy rate in selected years"
opt1_card2_label_bottom = "Comparison of the hotel occupancy rate among the selected years"

#Pass options to the menus ---- Card2
card2_menu_top_year = data.df_airbnb_homeway['AÑO'].unique()
opt1_card_options['opt1-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_top_year))

# --------Card 3 ------
opt1_card3_title = "Airbnb occupancy rate"
opt1_card3_subtitle = "Find out what is the occupancy rate of Airbnb properties in the city of Bogotá"

opt1_card3_label_top = "Average Airbnb occupancy rate in selected years"
opt1_card3_label_bottom = "Airbnb occupancy rate comparison among selected years"


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
                            value=opt1_card_options['opt1-board2-menu-top-year'][0]['value'],
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
                            # Menu Year segundo tablero
                            placeholder="Select the year",
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
