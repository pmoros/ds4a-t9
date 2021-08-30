import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap components
import dash_bootstrap_components as dbc

import data
import layouts

def create_options_dropdown(val):
    try:
        val_casted = str(val)
        label = val_casted
        value = val_casted

        my_dict = {}
        my_dict['label'] = label
        my_dict['value'] = value
    except:
        raise Exception("You're trying to use a binary object as label")

    return my_dict

#---- Common elements
banner_image = "https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/indicators-banner.jpg"

# --- Layout OPT1 (INDICATORS)

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
opt1_card_options['opt1-board1-row1-menu-left-year'] = list(map(create_options_dropdown, card1_menu_left_year))

# --------Card 2 ------
opt1_card2_title = "How old are the travelers?"
opt1_card2_subtitle = "Get to know the number of travelers that visit Bogotá city by age"

opt1_card2_label_left = "Age distribution of the total number of travelers who visited Bogotá in the selected years"
opt1_card2_label_right = "Comparison of the age distribution of travelers who visited Bogotá according to their origin"

#Pass options to the menus ---- Card2
card1_menu_left_year = data.df_airbnb_homeway['SUBTEMA'].unique()
opt1_card_options['opt1-board1-row1-menu-right-year'] = list(map(create_options_dropdown, card1_menu_left_year))

# --------Card 3 ------
opt1_card3_title = "What is the predominant gender among travelers?"
opt1_card3_subtitle = "Discover the number of travelers that visit Bogotá city by gender"

opt1_card3_label_left = "Gender distribution of the total number of travelers who visited Bogotá in the selected years"
opt1_card3_label_right = "Comparison of the gender of travelers who visited Bogotá according to their origin"

# --------Card 4 ------
opt1_card4_title = "What is the educational level of the travelers?"
opt1_card4_subtitle = "Find out the number of travelers that visit Bogotá city according to their educational level"

opt1_card4_label_top = "What is the occupation of the travelers?"
opt1_card4_label_bottom = "Get to know the number of travelers that visit Bogota city by occupation"


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


    ]
)
