#Card options for the user
opt1_card_options = {}

#Pass options to the menus ---- Card1

#Loading years
card1_menu_year = data.df_viajeros['AÑO'].unique()
opt1_card_options['board1-menu-year'] = list(map(layouts.create_options_dropdown, card1_menu_year))

#Loading months
card1_menu_month = data.df_viajeros['MES'].unique()
opt1_card_options['board1-menu-month'] = list(map(layouts.create_options_dropdown, card1_menu_month))



#Pass options to the menus ---- Card2
card2_menu_top_year = data.df_tasa_ocupacion_hotelera['AÑO'].unique()
opt1_card_options['opt1-board2-menu-top-year'] = list(map(layouts.create_options_dropdown, card2_menu_top_year))

#Pass options to the menus ---- Card2
card2_menu_bottom_year = data.df_tasa_ocupacion_hotelera['AÑO'].unique()
opt1_card_options['opt1-board2-menu-bottom-year'] = list(map(layouts.create_options_dropdown, card2_menu_bottom_year))


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
                        options=opt1_card_options['board1-menu-year'],
                        #BE AWARE OF SQUARE BRACKETS IN MULTI DROPDOWNS
                        value=[opt1_card_options['board1-menu-year'][0]['value']],
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
                        options=opt1_card_options['board1-menu-month'],
                        value=[opt1_card_options['board1-menu-month'][0]['value']],
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
                        id="opt1-board1-graph-right",
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
