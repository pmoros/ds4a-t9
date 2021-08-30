import dash_html_components as html
import dash_bootstrap_components as dbc


def get_main_banner(img_url, text_div):
    banner = dbc.Row(children=[
        dbc.Col(
            html.Div(
                children=[
                    text_div
                ],
                className="container-fluid main-banner row-full",
                style={'backgroundImage': '''url("{}")'''.format(img_url),
                       'backgroundPosition': "center"},
            ),
            width=12,
        ),
    ]
    )

    return banner

def get_main_banner_darker(img_url, text_div):
    banner = dbc.Row(children=[
        dbc.Col(
            html.Div(
                children=[
                    text_div
                ],
                className="container-fluid main-banner-darker row-full",
                style={'backgroundImage': '''url("{}")'''.format(img_url),
                       'backgroundPosition': "center"},
            ),
            width=12,
        ),
    ]
    )

    return banner    

def get_board_header(title, subtitle):
    my_header = dbc.Container([
        dbc.Row([
            html.H3(title, className="board-standard-header-title"),            
        ],
        justify="center",
        ),        
        dbc.Row([
            html.P(subtitle, className="board-standard-header-subtitle"),
        ],
        justify="center",
        ),
    ],
    fluid=True
    )

    return my_header