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
