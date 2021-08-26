
import dash_core_components as dcc
import dash_html_components as html


# Dash Bootstrap components
import dash_bootstrap_components as dbc


landingPage_title=["Bienvenidos", \
    "al sistema de informacion turistica de Bogotá"]
landingPage_subtitle=["En este sitio encontrarás \
    los principales datos de la demanda turística de Bogotá"]
landingPage = dbc.Container(
    children=[
    dbc.Row(children=[
        dbc.Col(
            html.Div(id="landing-text",
            children=[html.Div(
                id="landing-title",
                children=[
                    html.Span(html.H1(landingPage_title[0], className="landing-title-bold")),
                    html.Span(html.H1(landingPage_title[1], className="landing-title"))
                ],
                style={"margin-left": "10%", "margin-right": "10%"},
            ),
            html.Div(
                id="landing-subtitle",
                children=[
                    html.Span(html.P(landingPage_subtitle[0], className="landing-subtitle")),
                ],
                style={"margin-left": "10%", "margin-right": "10%"},
            )
            ],
            #className="container-fluid main-banner row-full",
            className="container-fluid landing-banner row-full",
            style={'background-image': '''url("assets/landing-image.png")'''}                        
            ),            
            width=12,
        ),
    ]
    ),

    ],
    fluid=True,
)
