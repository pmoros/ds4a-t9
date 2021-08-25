
import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap components
import dash_bootstrap_components as dbc

landingPage = dbc.Container(
    children=[
    dbc.Row(children=[
        html.Div(
            children=[html.Img(src="assets/landing_image.jpg", className="image-responsive")],
            className="header-banner",            
        )
    ]
    ),

    ]
)
