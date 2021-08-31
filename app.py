# import dash and bootstrap components
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components import Navbar
import dash_html_components as html
from dash.dependencies import Input, Output

# import dash IO and graph objects
from dash.dependencies import Input, Output

# Plotly graph objects to render graph plots
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

from index import *
import layouts_viajeros
import layouts_indicators

import data
import plotly.express as px

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


#----------------- Menu callback, set and return---------------------

# Declair function  that connects other pages with content to container
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname.endswith("/" or ""):
        return landingPage
    elif pathname.endswith(options_drop_navBar[options_navBar[1]][0]["value"]):
        return layouts_viajeros.opt1
    elif pathname.endswith(options_drop_navBar[options_navBar[1]][1]["value"]):
        return layouts_viajeros.opt2        
    elif pathname.endswith(options_drop_navBar[options_navBar[2]][0]["value"]):
        return layouts_indicators.opt1      
    elif pathname.endswith(options_drop_navBar[options_navBar[2]][1]["value"]):
        return layouts_indicators.opt2
    else:
        return "ERROR 404: Page not found!"


#-----------PAGES CALLBACKS ---------------------------
#-----------Indicadores (OPT1 [ACCOMODATION]) -----------------------

#Indicators-> ACCOMMODATION -> BOARD 1 -> GRAPH 1 (LEFT)
@app.callback(
    Output("opt1-board1-row1-graph-left", "figure")
,[
    Input("opt1-board1-row1-menu-left-year", "value"),
])
def update_indicators_opt1_b1_g1(selected_year):
    #SUMS 'VALOR' FOR EACH localidad, TOTALLY CRAZY DATA!!!
    #The plot doesn't make sense at all and doesn't mach the required plot, but
    #it is a good guide for people to use callbacks
    #The original menu returns multiple values, for this reason the plot breaks
    #if you select multiple values
    df_plot = data.df_airbnb_homeway[data.df_airbnb_homeway['AÑO'] == float(selected_year)]
    df_plot = df_plot.groupby('SUBTEMA').sum().reset_index()

    return px.bar(df_plot, x='SUBTEMA', y='VALOR')


#Indicators-> ACCOMMODATION (option 1) -> BOARD 1 -> GRAPH 2 (RIGHT)
@app.callback(
    Output("opt1-board1-row1-graph-right", "figure")
,[
    Input("opt1-board1-row1-menu-right-location", "value"),
])
def update_indicators_opt1_b1_g2(selected_locations):
    #Sample plot, THE PLOT IS WRONG, but its used for illustration
    df_plot = data.df_airbnb_homeway[data.df_airbnb_homeway['SUBTEMA'].isin(selected_locations)]
    df_plot = df_plot.groupby('SUBTEMA').mean().reset_index()

    return px.bar(df_plot, x='SUBTEMA', y='VALOR')


#Indicators-> ACCOMMODATION (option 1) -> BOARD 2 -> GRAPH 1 (TOP)
@app.callback(
    Output("opt1-board2-graph-top", "figure")
,[
    Input("opt1-board2-menu-top-year", "value"),
])
def update_indicators_opt1_b2_g1(selected_locations):

    df_plot = data.df_tasa_ocupacion_hotelera[data.df_tasa_ocupacion_hotelera['AÑO'].isin(selected_locations)]
    
    return px.line(df_plot, x='MES', y='VALOR', color='AÑO', line_group='AÑO')


#Indicators-> ACCOMMODATION (option 1) -> BOARD 3 -> GRAPH 1 (TOP)
@app.callback(
    Output("opt1-board3-graph-top", "figure")
,[
    Input("opt1-board3-menu-top-year", "value"),
])
def update_indicators_opt1_b3_g1(selected_locations):

    df_plot = data.df_tasa_ocupacion_airbnb[data.df_tasa_ocupacion_airbnb['AÑO'].isin(selected_locations)]
    
    return px.line(df_plot, x='MES', y='VALOR', color='AÑO', line_group='AÑO')


#-----------Indicadores (OPT2 [CONNECTIVITY]) -----------------------

#Indicators-> CONNECTIVITY -> BOARD 1 -> GRAPH 1
@app.callback(
    Output("opt2-board1-graph", "figure")
,[
    Input("opt2-board1-menu-year", "value"),
])
def update_indicators_opt2_b1_g1(selected_year):

    df_plot = data.df_bigdata[data.df_bigdata['AÑO'].isin([selected_year])]

    return px.bar(df_plot, x='SUBTEMA', y='VALOR', color='VARIABLE', facet_col='AÑO')


#Indicators-> CONNECTIVITY -> BOARD 2 -> GRAPH 1
@app.callback(
    Output("opt2-board2-graph", "figure")
,[
    Input("opt2-board2-menu-year", "value"),
])
def update_indicators_opt2_b2_g1(selected_item):

    df_plot = df_conect_internacional[df_conect_internacional['SUBTEMA'] == selected_item]

    return px.bar(df_plot, x='AÑO', y='VALOR', color='AÑO')


#Indicators-> CONNECTIVITY -> BOARD 3 -> GRAPH 1
@app.callback(
    Output("opt2-board3-graph", "figure")
,[
    Input("opt2-board3-menu-year", "value"),
])
def update_indicators_opt2_b3_g1(selected_item):

    df_plot = df_turismo_internacional[df_turismo_internacional['VARIABLE'] == selected_item]

    return px.line(df_plot, x='AÑO', y='VALOR', color='SUBTEMA', line_group='SUBTEMA')

#Indicators-> CONNECTIVITY -> BOARD 4 -> GRAPH 1
@app.callback(
    Output("opt2-board4-graph", "figure")
,[
    Input("opt2-board4-menu-year", "value"),
])
def update_indicators_opt2_b4_g1(selected_item):

    df_plot = df_turismo_internacional2[df_turismo_internacional2['VARIABLE'] == selected_item]

    return px.area(df_plot, x='AÑO', y='VALOR', color='CLASE', line_group='CLASE')


#-----------Travelers - OPT1 (WHO THEY ARE) -----------------------

#THIS IS A TEST GRAPH!!!!!
#------------- BOARD 1 -------------------
#Travelers -> OPT1 -> BOARD 1 -> GRAPH 1 (LEFT)
@app.callback(
    Output("opt1-board1-graph-left", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    Input("viajeros-selector-both", "n_clicks_timestamp")
])
def update_indicators_opt1_b1_g2(national_bt, international_bt, both_bt):
    # USING TYPE OF TOURIST FILTER
    if int(national_bt) > int(international_bt) and int(national_bt) > int(both_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) and int(international_bt) > int(both_bt):
        category = "TURISTAS INTERNACIONALES"
    elif int(both_bt) > int(national_bt) and int(both_bt) > int(international_bt):
        category = "both"
    else:
        category = "national"

    #CREATING THE REQUIRED FILTER
    df_plot = data.df_viajeros
    if category != "both":        
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == category]

    #df_plot = data.df_viajeros[data.df_viajeros['SUBTEMA'] == "MOTIVO"]        

    #df_plot = df_plot.groupby('ITEM').sum().reset_index()
    df_plot = df_plot.groupby('TEMA').sum().reset_index()

    #CREATION OF THE PLOT + RETURN OF IT
    return px.bar(df_plot, x='TEMA', y='VIAJEROS')

#------------------ BOARD 2 ----------------

#Travelers -> OPT1 -> BOARD 2 -> MENU -> RIGHT -> ORIGIN




#--------------------LAYOUT DECLARATION-------------------------

app.layout = index()



# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
