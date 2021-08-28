# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components import Navbar
import dash_html_components as html
from dash.dependencies import Input, Output

from index import *
import layouts_viajeros


# Alternative 1
MAIN_COLOR_SELECTOR = "#6C7BC4"
# Alternative 2
MAIN_COLOR_SELECTOR = "#7484d4"

landingPage_title = ["Welcome", "to the Bogotá tourist information system"]
landingPage_subtitle = [
    "In this site you will find the main data on the tourist demand of Bogotá"]
landingPage = dbc.Container(
    children=[
        dbc.Row(children=[
            dbc.Col(
                html.Div(id="landing-text",
                         children=[html.Div(
                             id="landing-title",
                             children=[
                                 html.Span(
                                     html.H1(landingPage_title[0], className="landing-title-bold")),
                                 html.Span(
                                     html.H1(landingPage_title[1], className="landing-title"))
                             ],
                             style={"marginLeft": "10%", "marginRight": "10%"},
                         ),
                             html.Div(
                             id="landing-subtitle",
                             children=[
                                 html.Span(
                                     html.P(landingPage_subtitle[0], className="landing-subtitle")),
                             ],
                             style={"marginLeft": "10%", "marginRight": "10%"},
                         )
                         ],
                         #className="container-fluid main-banner row-full",
                         className="container-fluid landing-banner row-full",
                         style={
                             'backgroundImage': '''url("https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/assets-static/landing-image.png")'''}
                         #style={'background-image': '''url("assets/landing-image.png")'''}
                         ),
                width=12,
            ),
        ]
        ),

    ],
    fluid=True,
)

# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SANDSTONE],
    meta_tags=[{"name": "viewport",
                "content": "width=device-width, initial-scale=1"}],
)

# set app title
app.title = "IDT Dashboard"

# set app server to variable for deployment
server = app.server

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

# Main index function that will call and return all layout variables


def index():

    layout = html.Div([header, navBar, container, footer])
    return layout


# Menu callback, set and return
# Declair function  that connects other pages with content to container
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname.endswith("/" or ""):
        return landingPage
    elif pathname.endswith(options_drop_navBar[options_navBar[1]][0]["value"]):
        return layouts_viajeros.opt1
    elif pathname.endswith(options_drop_navBar[options_navBar[1]][1]["value"]):
        return layouts_viajeros.opt2        
    else:
        return "ERROR 404: Page not found!"


app.layout = index()

# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
