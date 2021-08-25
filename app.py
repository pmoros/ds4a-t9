# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components import Navbar
import dash_html_components as html
from dash.dependencies import Input, Output

from index import *
import layouts

# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SANDSTONE],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

# set app title
app.title = "IDT Dashboard"

# set app server to variable for deployment
srv = app.server

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True

# Main index function that will call and return all layout variables
def index():
    #layout = html.Div([index.header, index.nav, index.container, index.footer])
    #layout = html.Div([header, container, footer])
    #layout = html.Div([header, navBar, footer])
    layout = html.Div([header, navBar, container, footer])
    return layout


# Menu callback, set and return
# Declair function  that connects other pages with content to container
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname.endswith("/"):
        return layouts.landingPage
    else:
        return "ERROR 404: Page not found!"

app.layout = index()

# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
