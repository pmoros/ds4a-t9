import dash_html_components as html
import dash_core_components as dcc

import dash_bootstrap_components as dbc

import layouts

#-----Page title layout
about_us_page_title = html.Div([  
    dbc.Row([
        dbc.Col([
            dbc.Row([                
                html.H1([
                    html.Span("Our ", className="font-title-3-blue"),
                    html.Span("work team", className="font-title-3-green")
                ]
                )                
            ],
            justify='center'
            )

        ],
        xs={'size': 6, 'offset': 3},        
        sm={'size': 6, 'offset': 3},        
        md={'size': 6, 'offset': 0},
        lg={'size': 6, 'offset': 0},

        className="margin-space-1-top",
        id="page-title"
        )

    ],
    ),

    dbc.Row([
        html.Div([
            html.P("We are an interdisciplinary group with a passion for data science.\
            We process information to make strategic decisions and solve society problems.",
            className="font-subtitle-2")
        ],
        className="content-center-left"        
        )            
    ],    
    ),

    dbc.Row([
        html.Div([
            html.P(html.I("\"Without data you are just another person with an opinion\"")),
            html.P("W. Edwards deming"),         
        ],

        className="quote-right font-subtitle-3",
        )
    ],

    className="margin-space-1-top content-center-left d-flex justify-content-end"
    
    ),

    dbc.Row([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/ElizabethRendonPic.png", className="thumbnail-team-dimension"),
                    html.Div([html.P(html.B("Elizabeth Rendón")),
                            html.P("Medellín"),
                            html.P("PhD. Mechanical Engineer"),
                            html.P("Working at Universidad EAFIT"),
                            ],

                            className="team-member-info"
                            )
                ],

                className="team-member-container"
                )
            ],

            
            md={"size": 4},

            ),

            dbc.Col([
                html.Div([
                    html.Img(src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/SergioRairanPic.png", className="thumbnail-team-dimension"),
                    html.Div([html.P(html.B("Sergio Rairán")),
                            html.P("Bogotá"),
                            html.P("Statistician"),
                            html.P("Working at Experian Colombia"),
                            ],

                            className="team-member-info"
                            )
                ],

                className="team-member-container"
                )
            ],

            
            md={"size": 4},

            ),

            dbc.Col([
                html.Div([
                    html.Img(src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/AlbertoCortesPic.png", className="thumbnail-team-dimension"),
                    html.Div([html.P(html.B("Alberto Cortés")),
                            html.P("Valledupar"),
                            html.P("Electronic Engineer"),
                            html.P("Control Specialist at Primax Colombia"),
                            ],

                            className="team-member-info"
                            )
                ],

                className="team-member-container"
                )
            ],

            
            md={"size": 4},

            ),                        
        ]
        ),

        dbc.Row([
            dbc.Col([
                html.Div([
                    html.Img(src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/DiegoCabreraPic.png", className="thumbnail-team-dimension"),
                    html.Div([html.P(html.B("Diego Cabrera")),
                            html.P("Manizales"),
                            html.P("Electronic Engineer"),
                            html.P("PhD. Student at Tecnológico de Monterrey"),
                            ],

                            className="team-member-info"
                            )
                ],

                className="team-member-container"
                )
            ],

            
            md={"size": 4},

            ),

            dbc.Col([
                html.Div([
                    html.Img(src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/PaulMorosPic.png", className="thumbnail-team-dimension"),
                    html.Div([html.P(html.B("Paul Moros")),
                            html.P("Bogotá"),
                            html.P("Systems Engineering Student at Universidad Nacional de Colombia"),
                            ],

                            className="team-member-info"
                            )
                ],

                className="team-member-container"
                )
            ],

            
            md={"size": 4},

            ),

            dbc.Col([
                html.Div([
                    html.Img(src="https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/KellyGarciaPic.png", className="thumbnail-team-dimension"),
                    html.Div([html.P(html.B("Kelly García")),
                            html.P("Garzón-Huila"),
                            html.P("Economist"),
                            html.P("Working at Universidad Compensar"),
                            ],

                            className="team-member-info"
                            )
                ],

                className="team-member-container"
                )
            ],

            
            md={"size": 4},

            ),                        
        ],

        className="margin-space-1-top",
        ),

    ],
    className="margin-space-1-top margin-space-2-bottom content-center-left"
    ),

    #layouts.get_main_banner_empty("https://static.wixstatic.com/media/1fc02c_55258d4962d244db905eded1d73ffed3~mv2.jpg/v1/fill/w_1909,h_439,al_c,q_85,usm_0.66_1.00_0.01/1fc02c_55258d4962d244db905eded1d73ffed3~mv2.webp")    

],

)


#-----Layout for the user
about_us_layout = dbc.Container([
    about_us_page_title,
],
fluid=True,
)
