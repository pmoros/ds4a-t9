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
import layouts_about_us

import data

# Alternative 1
MAIN_COLOR_SELECTOR = "#6C7BC4"
# Alternative 2
MAIN_COLOR_SELECTOR = "#7484d4"

COLOR_PALETTE_DISCRETE = ["#20284D", "#4A589B","#D4D4E9", "#BADA55", "#FFE787", "#B8B97E","#D36135","#F49D6E","#4C8577"]#px.colors.qualitative.T10
COLOR_PALETTE_CONTINUOUS = ["#20284D", "#4A589B","#D4D4E9", "#BADA55"]

MESES_ORDEN = {'Enero':1, 'Febrero':2, 'Marzo':3, 'Abril':4, 'Mayo':5,'Junio':6,
       'Julio':7, 'Agosto':8, 'Septiembre':9, 'Octubre':10,'Noviembre':11,'Diciembre':12}


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
    elif pathname.endswith(options_drop_navBar[options_navBar[2]][2]["value"]):
        return layouts_indicators.opt3
    elif pathname.endswith(options_drop_navBar[options_navBar[2]][3]["value"]):
        return layouts_indicators.opt4
    elif pathname.endswith("/about-us"):
        return layouts_about_us.about_us_layout
    else:
        return "ERROR 404: Page not found!"


#-----------PAGES CALLBACKS ---------------------------
#-----------Indicadores (OPT1 [ACCOMODATION]) -----------------------

#Indicators-> ACCOMMODATION -> BOARD 1 -> GRAPH 1 (TOP)
@app.callback(
    Output("opt1-board1-graph-top", "figure")
,[
    Input("opt1-board1-menu-top-year", "value"),
])
def update_indicators_opt1_b1_g1(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_airbnb_homeway[data.df_airbnb_homeway['AÑO'].isin(selected_year)]
    df_plot = df_plot.groupby('SUBTEMA').sum().reset_index()

    fig = px.bar(df_plot, x='SUBTEMA', y='VALOR',color='SUBTEMA',
             labels={
                'VALOR': "Value", 'SUBTEMA': "Location"
            },
             color_discrete_sequence=COLOR_PALETTE_DISCRETE,

            )
    fig.update_xaxes(showticklabels=True) # hide all the xticks
    fig.update_layout(showlegend=False)
    return fig

#Indicators-> ACCOMMODATION (option 1) -> BOARD 1 -> GRAPH 2 (BOTTOM)
@app.callback(
    Output("opt1-board1-graph-bottom", "figure")
,[
    Input("opt1-board1-menu-bottom-year", "value"),
])
def update_indicators_opt1_b1_g2(selected_locations):

    df_plot = data.df_airbnb_homeway[data.df_airbnb_homeway['SUBTEMA'].isin(selected_locations)]
    df_plot = df_plot.groupby('SUBTEMA').mean().reset_index()

    fig = px.bar(df_plot, x='SUBTEMA', y='VALOR',color='SUBTEMA',
             labels={
                'VALOR': "Value", 'SUBTEMA': "Location"
            },
             color_discrete_sequence=COLOR_PALETTE_DISCRETE,


            )
    fig.update_traces(width=0.5)
    fig.update_layout(showlegend=False)
    return fig

#Indicators-> ACCOMMODATION (option 1) -> BOARD 2 -> GRAPH 1 (TOP)
@app.callback(
    Output("opt1-board2-graph-top", "figure")
,[
    Input("opt1-board2-menu-top-year", "value"),
])
def update_indicators_opt1_b2_g1(selected_year):

    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_tasa_ocupacion_hotelera[data.df_tasa_ocupacion_hotelera['AÑO'].isin(selected_year)]
    df_plot = df_plot.groupby('MES').mean().reset_index()
    df_plot['MESNO'] = df_plot['MES'].replace(MESES_ORDEN)
    df_plot = df_plot.sort_values(by=['MESNO'])

    fig = px.line(df_plot, x='MES', y='VALOR',
            labels={
                'VALOR': "Value (%)", 'AÑO': "Year", 'MES': "Month"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,

            )
    fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
                          'Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
        ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                          'AUG','SEP','OCT','NOV','DEC']
    )
)

    return fig

#Indicators-> ACCOMMODATION (option 1) -> BOARD 2 -> GRAPH 1 (BOTTOM)
@app.callback(
    Output("opt1-board2-graph-bottom", "figure")
,[
    Input("opt1-board2-menu-bottom-year", "value"),
])
def update_indicators_opt1_b2_g2(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_tasa_ocupacion_hotelera[data.df_tasa_ocupacion_hotelera['AÑO'].isin(selected_year)]

    fig = px.line(df_plot, x='MES', y='VALOR', color='AÑO', line_group='AÑO',
             labels={
                'VALOR': "Value (%)", 'AÑO': "Year", 'MES': "Month"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,

            )
    fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio',
                          'Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
        ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                          'AUG','SEP','OCT','NOV','DEC']
    )
)

    return fig

#Indicators-> ACCOMMODATION (option 1) -> BOARD 3 -> GRAPH 1 (TOP)
@app.callback(
    Output("opt1-board3-graph-top", "figure")
,[
    Input("opt1-board3-menu-top-year", "value"),
])
def update_indicators_opt1_b3_g1(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_tasa_ocupacion_airbnb[data.df_tasa_ocupacion_airbnb['AÑO'].isin(selected_year)]
    df_plot = df_plot.groupby('MES').mean().reset_index()
    # print(df_plot)

    fig = px.line(df_plot, x='MES', y='VALOR',
             labels={
                'VALOR': "Value (%)", 'AÑO': "Year", 'MES': "Month"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,

            )
    fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['1','2','3','4','5','6','7',
                          '8','9','10','11','12'],
        ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                          'AUG','SEP','OCT','NOV','DEC']
    )
)
    return fig

#Indicators-> ACCOMMODATION (option 1) -> BOARD 3 -> GRAPH 1 (BOTTOM)
@app.callback(
    Output("opt1-board3-graph-bottom", "figure")
,[
    Input("opt1-board3-menu-bottom-year", "value"),
])
def update_indicators_opt1_b3_g2(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_tasa_ocupacion_airbnb[data.df_tasa_ocupacion_airbnb['AÑO'].isin(selected_year)]

    fig = px.line(df_plot, x='MES', y='VALOR', color='AÑO', line_group='AÑO',
             labels={
                'VALOR': "Value (%)", 'AÑO': "Year", 'MES': "Month"
            },
            # template='ggplot2',
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,

            )
    # fig.layout.plot_bgcolor = 'rgb(255,255,255)'
    fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['1','2','3','4','5','6','7',
                          '8','9','10','11','12'],
        ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                          'AUG','SEP','OCT','NOV','DEC']
    )
)
    return fig

#-----------Indicadores (OPT2 [CONNECTIVITY]) -----------------------

#Indicators-> CONNECTIVITY -> BOARD 1 -> GRAPH 1
@app.callback(
    Output("opt2-board1-graph", "figure")
,[
    Input("opt2-board1-menu-year", "value"),
])
def update_indicators_opt2_b1_g1(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_bigdata[data.df_bigdata['AÑO'].isin(selected_year)]

    fig = px.bar(df_plot, x='SUBTEMA', y='VALOR', color='VARIABLE', facet_col='AÑO',
             labels={
                'SUBTEMA': "Country",  'AÑO': "Year", 'VALOR': "Total"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,

            )
    fig.update_layout(legend_title="Category")

    return fig


#Indicators-> CONNECTIVITY -> BOARD 2 -> GRAPH 1
@app.callback(
    Output("opt2-board2-graph", "figure")
,[
    Input("opt2-board2-menu-year", "value"),
])
def update_indicators_opt2_b2_g1(selected_item):

    df_plot = data.df_conect_internacional[data.df_conect_internacional['SUBTEMA'] == selected_item]
    variable = df_plot['VARIABLE'].iloc[0]

    fig = px.bar(df_plot, x='AÑO', y='VALOR', color='AÑO',
             labels={
                'VALOR': variable, 'AÑO': "Year"
            },
             color_continuous_scale=COLOR_PALETTE_CONTINUOUS,
            )
    fig.update_layout(legend_title="Continent")

    return fig


#Indicators-> CONNECTIVITY -> BOARD 3 -> GRAPH 1
@app.callback(
    Output("opt2-board3-graph-top", "figure")
,[
    Input("opt2-board3-menu-top-year", "value"),
])
def update_indicators_opt2_b3_g1(selected_item):

    df_plot = data.df_turismo_internacional[data.df_turismo_internacional['VARIABLE'] == selected_item]
    clase = df_plot['CLASE'].iloc[0]

    fig = px.line(df_plot, x='AÑO', y='VALOR', color='SUBTEMA', line_group='SUBTEMA',
             labels={
                'VALOR': clase, 'AÑO': "Year"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )
    fig.update_layout(legend_title="Continent")

    return fig


#Indicators-> CONNECTIVITY -> BOARD 3 -> GRAPH 2
@app.callback(
    Output("opt2-board3-graph-bottom", "figure")
,[
    Input("opt2-board3-menu-bottom-year", "value"),
])
def update_indicators_opt2_b3_g2(selected_item):

    df_plot = data.df_turismo_internacional2[data.df_turismo_internacional2['VARIABLE'] == selected_item]

    fig = px.area(df_plot, x='AÑO', y='VALOR', color='CLASE', line_group='CLASE',
             labels={
                'VALOR': "Value (%)", 'AÑO': "Year"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,

            )
    fig.update_layout(legend_title="Category")

    return fig

#-----------Indicadores (OPT3 [ECONOMIC]) -----------------------

#Indicators-> ECONOMIC -> BOARD 2 -> GRAPH 1
@app.callback(
    Output("opt3-board2-graph-top", "figure")
,[
    Input("opt3-board2-menu-top-year", "value"),
])
def update_indicators_opt3_b2_g1(selected_item):

    df_plot = data.df_gen_empleo_turismo[data.df_gen_empleo_turismo['SUBTEMA'] == selected_item]

    fig = px.line(df_plot, x='AÑO', y='VALOR', color='VARIABLE', line_group='VARIABLE',
             labels={
                'VALOR': "Jobs", 'AÑO': "Year"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )
    fig.update_traces(mode='markers+lines')
    fig.update_layout(legend_title="Category")
    return fig

#Indicators-> ECONOMIC -> BOARD 2 -> GRAPH 2
@app.callback(
    Output("opt3-board2-graph-bottom", "figure")
,[
    Input("opt3-board2-menu-bottom-year", "value"),
])
def update_indicators_opt3_b2_g2(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_gen_empleo_turismo2[data.df_gen_empleo_turismo2['AÑO'].isin(selected_year)]

    fig = px.line(df_plot, x='MES', y='VALOR', color='AÑO', line_group='AÑO',
             labels={
                'VALOR': "Jobs", 'AÑO': "Year", 'MES': "Quarter",
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )
    fig.update_traces(mode='markers+lines')

    return fig

#-----------Indicadores (OPT4 [SIGHTSEEING]) -----------------------

#Indicators-> SIGHTSEEING -> BOARD 1 -> GRAPH 1
@app.callback(
    Output("opt4-board1-graph", "figure")
,[
    Input("opt4-board1-menu-year", "value"),
])
def update_indicators_opt4_b1_g1(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_cert_turismo_sostenible[data.df_cert_turismo_sostenible['AÑO'].isin(selected_year)]

    fig = px.bar(df_plot, x='VARIABLE', y='VALOR', color='VARIABLE',
             labels={
                'VARIABLE': "Establishment Type", 'VALOR': "Total",
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )
    fig.update_xaxes(showticklabels=False) # hide all the xticks
    return fig

#Indicators-> SIGHTSEEING -> BOARD 2 -> GRAPH 1
@app.callback(
    Output("opt4-board2-graph-top", "figure")
,[
    Input("opt4-board2-menu-top-year", "value"),
])
def update_indicators_opt4_b2_g1(selected_item):

    df_plot = data.df_prest_servicios_turisticos1[data.df_prest_servicios_turisticos1['SUBTEMA'].isin(selected_item)]

    fig = px.line(df_plot, x='AÑO', y='VALOR', color='SUBTEMA', line_group='SUBTEMA',
             labels={
                'VALOR': "Total", 'AÑO': "Year", 'SUBTEMA': "Provider"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )

    return fig

#Indicators-> SIGHTSEEING -> BOARD 2 -> GRAPH 2
@app.callback(
    Output("opt4-board2-graph-bottom", "figure")
,[
    Input("opt4-board2-menu-bottom-year", "value"),
])
def update_indicators_opt4_b2_g2(selected_item):

    df_plot = data.df_prest_servicios_turisticos2[data.df_prest_servicios_turisticos2['SUBTEMA'].isin(selected_item)]

    fig = px.line(df_plot, x='AÑO', y='VALOR', color='SUBTEMA', line_group='SUBTEMA',
             labels={
                'VALOR': "Total", 'AÑO': "Year", 'SUBTEMA': "Provider"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )

    return fig

#Indicators-> SIGHTSEEING -> BOARD 3 -> GRAPH 1
@app.callback(
    Output("opt4-board3-graph", "figure")
,[
    Input("opt4-board3-menu-year", "value"),
])
def update_indicators_opt4_b3_g1(selected_year):
    selected_year = [int(x) for x in selected_year]
    df_plot = data.df_indice_competitividad_turistica[data.df_indice_competitividad_turistica['AÑO'].isin(selected_year)]

    fig = px.bar_polar(df_plot, r='VALOR', theta='VARIABLE', color='AÑO', template='plotly_white',
             labels={
                'VALOR': "Indice", 'AÑO': "Year", 'VARIABLE': "Category"
            },
            color_continuous_scale=COLOR_PALETTE_CONTINUOUS,
            )

    fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
    fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

    return fig

#-----------Travelers - Common selectors ----------


#----------SELECTOR VALUES LOAD---------------

#----------LOAD MAIN CARD--------------
#Same main card for all OPT, this works for all of them

@app.callback(
    Output("main-board-menu-year", "options"),
    Output("main-board-menu-month", "options"),
    Output("main-board-menu-year", "value"),
    Output("main-board-menu-month", "value")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_main_board_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_month = data.df_viajeros_nacional['MES'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_month = data.df_viajeros_internacional['MES'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_month = list(map(layouts.create_options_dropdown, menu_month))

    return menu_year, menu_month, [menu_year[0]['value']], [menu_month[0]['value']]




#-----------Travelers - OPT1 (WHO THEY ARE) -----------------------

#-----------MENUS LOAD -------------------

#-----------Load menu OPT1->BOARD2
@app.callback(
    Output("travelers_opt1-board2-row1-menu-left-year", "options"),
    Output("travelers_opt1-board2-row1-menu-right-year", "options"),
    Output("travelers_opt1-board2-row1-menu-right-origin", "options"),
    Output("travelers_opt1-board2-row1-menu-left-year", "value"),
    Output("travelers_opt1-board2-row1-menu-right-year", "value"),
    Output("travelers_opt1-board2-row1-menu-right-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt1_board2_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], menu_year[0]['value'], [menu_origin[0]['value']]

#-----------Load menu OPT1->BOARD3
@app.callback(
    Output("travelers_opt1-board3-row1-menu-left-year", "options"),
    Output("travelers_opt1-board3-row1-menu-right-year", "options"),
    Output("travelers_opt1-board3-row1-right-origin", "options"),
    Output("travelers_opt1-board3-row1-menu-left-year", "value"),
    Output("travelers_opt1-board3-row1-menu-right-year", "value"),
    Output("travelers_opt1-board3-row1-right-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt1_board3_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], menu_year[0]['value'], [menu_origin[0]['value']]



#-----------Load menu OPT1->BOARD4
@app.callback(
    Output("travelers_opt1-board4-menu-top-year", "options"),
    Output("travelers_opt1-board4-menu-bottom-year", "options"),
    Output("travelers_opt1-board4-bottom-origin", "options"),
    Output("travelers_opt1-board4-menu-top-year", "value"),
    Output("travelers_opt1-board4-menu-bottom-year", "value"),
    Output("travelers_opt1-board4-bottom-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt1_board4_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], [menu_year[0]['value']], [menu_origin[0]['value']]


#-----------Load menu OPT1->BOARD5
@app.callback(
    Output("travelers_opt1-board5-menu-top-year", "options"),
    Output("travelers_opt1-board5-menu-bottom-year", "options"),
    Output("travelers_opt1-board5-bottom-origin", "options"),
    Output("travelers_opt1-board5-menu-top-year", "value"),
    Output("travelers_opt1-board5-menu-bottom-year", "value"),
    Output("travelers_opt1-board5-bottom-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt1_board5_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], menu_year[0]['value'], [menu_origin[0]['value']]

#-------------------BOARDS WITHS GRAPHS---------------

#------------- BOARD 1 -------------------

#-----------Load menu OPT1->BOARD1
@app.callback(
    Output("board1-menu-year", "options"),
    Output("board1-menu-month", "options"),
    Output("board1-menu-year", "value"),
    Output("board1-menu-month", "value")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_board1_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_month = data.df_viajeros_nacional['MES'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_month = data.df_viajeros_internacional['MES'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_month = list(map(layouts.create_options_dropdown, menu_month))

    return menu_year, menu_month, [menu_year[0]['value']], [menu_month[0]['value']]




#Travelers -> OPT1 -> BOARD 1 -> GRAPH

@app.callback(
    Output("travelers_opt1-board1-graph-right", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    Input("board1-menu-year", "value"),
    Input("board1-menu-month", "value")
])

def update_travelers_opt1_b1_g2(national_bt, international_bt, years, months):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        my_plot = data.viajeros_region_nacional_plot(years, months)
    elif category == "TURISTAS INTERNACIONALES":
        my_plot = data.viajeros_region_internacional_plot(years, months)

    return my_plot

#------------------ BOARD 2 ----------------
#Travelers -> OPT1 -> BOARD 2 GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt1-board2-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    

    Input("travelers_opt1-board2-menu-top-year", "value"),
])
def update_travelers_travelers_opt1_b2_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass


    selected_year = [int(x) for x in selected_year]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'EDAD']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['ITEM']=='A. NS/NR'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar(df_plot,
                       x = 'VIAJEROS', y = 'MES', color = 'ITEM',
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig       


#Travelers -> OPT1 -> BOARD 2 GRAPH 2 (BOTTOM)
@app.callback(
    Output("travelers_opt1-board2-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt1-board2-menu-bottom-year", "value"),
    Input("travelers_opt1-board2-bottom-origin", "value"),
])
def update_travelers_travelers_opt1_b2_g2(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'EDAD']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['ITEM']=='A. NS/NR'].index)

    fig = px.line(df_plot, x = 'MES', y = 'VIAJEROS', color = 'ITEM', line_dash = 'ORIGEN',
                 color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                 category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                  labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'PURPOSE, ORIGIN','ORIGEN':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig

#------------------ BOARD 3 ----------------
#Travelers -> OPT1 -> BOARD 3 GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt1-board3-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    

    Input("travelers_opt1-board3-menu-top-year", "value"),
])
def update_travelers_travelers_opt1_b3_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass


    selected_year = [int(x) for x in selected_year]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'GENERO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['ITEM']=='C. NS/NR'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar(df_plot,
                       x = 'VIAJEROS', y = 'MES', color = 'ITEM', barmode="group",
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig       


#Travelers -> OPT1 -> BOARD 3 GRAPH 2 (BOTTOM)
@app.callback(
    Output("travelers_opt1-board3-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt1-board3-menu-bottom-year", "value"),
    Input("travelers_opt1-board3-bottom-origin", "value"),
])
def update_travelers_travelers_opt1_b3_g2(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'GENERO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['ITEM']=='C. NS/NR'].index)

    fig = px.line(df_plot, x = 'MES', y = 'VIAJEROS', color = 'ITEM', line_dash = 'ORIGEN',
                 color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                 category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                  labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'PURPOSE, ORIGIN','ORIGEN':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig

#------------------ BOARD 4 ----------------
#Travelers -> OPT1 -> BOARD 4 GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt1-board4-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    

    Input("travelers_opt1-board3-menu-top-year", "value"),
])
def update_travelers_travelers_opt1_b4_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass


    selected_year = [int(x) for x in selected_year]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'EDUCATION']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['ITEM']=='G. NS/NR'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar(df_plot,
                       x = 'MES', y = 'VIAJEROS', color = 'ITEM',
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig       


#Travelers -> OPT1 -> BOARD 4 GRAPH 2 (BOTTOM)
@app.callback(
    Output("travelers_opt1-board4-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt1-board4-menu-bottom-year", "value"),
    Input("travelers_opt1-board4-bottom-origin", "value"),
])
def update_travelers_travelers_opt1_b4_g2(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'EDUCATION']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['ITEM']=='G. NS/NR'].index)

    fig = px.bar(df_plot,
                       x = 'MES', y = 'VIAJEROS', color = 'ITEM',
                       pattern_shape="ORIGEN", 
                       pattern_shape_sequence=[".", "+"],
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig


#--------------LOAD MENU BOARDS-----------

#------------------ BOARD 3 ----------------

#-----------Load menu OPT2->BOARD3
@app.callback(
    Output("travelers_opt2-board3-menu-top-year", "options"),
    Output("travelers_opt2-board3-menu-bottom-year", "options"),
    Output("travelers_opt2-board3-bottom-origin", "options"),
    Output("travelers_opt2-board3-menu-top-year", "value"),
    Output("travelers_opt2-board3-menu-bottom-year", "value"),
    Output("travelers_opt2-board3-bottom-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt2_board3_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], [menu_year[0]['value']], [menu_origin[0]['value']]


#------------------ BOARD 4 ----------------

#-----------Load menu OPT2->BOARD4
@app.callback(
    Output("travelers_opt2-board4-row1-menu-left-year", "options"),
    Output("travelers_opt2-board4-row1-menu-right-year", "options"),
    Output("travelers_opt2-board4-row1-menu-right-origin", "options"),
    Output("travelers_opt2-board4-row1-menu-left-year", "value"),
    Output("travelers_opt2-board4-row1-menu-right-year", "value"),
    Output("travelers_opt2-board4-row1-menu-right-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt2_board4_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], menu_year[0]['value'], [menu_origin[0]['value']]


#------------------ BOARD 5 ----------------

#-----------Load menu OPT2->BOARD5
@app.callback(
    Output("travelers_opt2-board5-row1-menu-left-year", "options"),
    Output("travelers_opt2-board5-row1-menu-right-year", "options"),
    Output("travelers_opt2-board5-row1-menu-right-origin", "options"),
    Output("travelers_opt2-board5-row1-menu-left-year", "value"),
    Output("travelers_opt2-board5-row1-menu-right-year", "value"),
    Output("travelers_opt2-board5-row1-menu-right-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt2_board5_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], menu_year[0]['value'], [menu_origin[0]['value']]


#------------------ BOARD 6 ----------------

#-----------Load menu OPT2->BOARD6
@app.callback(
    Output("travelers_opt2-board6-row1-menu-left-year", "options"),
    Output("travelers_opt2-board6-row1-menu-right-year", "options"),
    Output("travelers_opt2-board6-row1-menu-right-origin", "options"),
    Output("travelers_opt2-board6-row1-menu-left-year", "value"),
    Output("travelers_opt2-board6-row1-menu-right-year", "value"),
    Output("travelers_opt2-board6-row1-menu-right-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt2_board6_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], menu_year[0]['value'], [menu_origin[0]['value']]


#------------------ BOARD 7 ----------------

#-----------Load menu OPT2->BOARD7
@app.callback(
    Output("travelers_opt2-board7-row1-menu-left-year", "options"),
    Output("travelers_opt2-board7-row1-menu-right-year", "options"),
    Output("travelers_opt2-board7-row1-menu-right-origin", "options"),
    Output("travelers_opt2-board7-row1-menu-left-year", "value"),
    Output("travelers_opt2-board7-row1-menu-right-year", "value"),
    Output("travelers_opt2-board7-row1-menu-right-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt2_board7_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], menu_year[0]['value'], [menu_origin[0]['value']]



#Travelers -> OPT1 -> BOARD 2 -> MENU -> RIGHT -> ORIGIN


#-----------Travelers - OPT2 (WHAT THEY PREFER) -----------------------

#------------------ BOARD 1 ----------------
#-----------Load menu OPT2->BOARD1
@app.callback(
    Output("travelers_opt2-board1-menu-top-year", "options"),
    Output("travelers_opt2-board1-menu-bottom-year", "options"),
    Output("travelers_opt2-board1-bottom-origin", "options"),
    Output("travelers_opt2-board1-menu-top-year", "value"),
    Output("travelers_opt2-board1-menu-bottom-year", "value"),
    Output("travelers_opt2-board1-bottom-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt2_board1_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], [menu_year[0]['value']], [menu_origin[0]['value']]



#Travelers -> OPT2 -> BOARD 1 -> trip purpose: GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt2-board1-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    

    Input("travelers_opt2-board1-menu-top-year", "value"),
])
def update_travelers_travelers_opt2_b1_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass


    selected_year = [int(x) for x in selected_year]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'MOTIVO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar(df_plot,
                       x = 'MES', y = 'VIAJEROS', color = 'ITEM',
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig       


#Travelers -> OPT2 -> BOARD 1 -> trip purpose: GRAPH 2 (BOTTON)
@app.callback(
    Output("travelers_opt2-board1-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board1-menu-bottom-year", "value"),
    Input("travelers_opt2-board1-bottom-origin", "value"),
])
def update_travelers_travelers_opt2_b1_g2(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'MOTIVO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)

    fig = px.line(df_plot, x = "MES", y = "VIAJEROS", color = "ITEM", line_dash = 'ORIGEN',
                 color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                 category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                  labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'PURPOSE, ORIGIN','ORIGEN':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig

#------------------ BOARD 2 ----------------

#-----------Load menu OPT2->BOARD2
@app.callback(
    Output("travelers_opt2-board2-menu-top-year", "options"),
    Output("travelers_opt2-board2-menu-bottom-year", "options"),
    Output("travelers_opt2-board2-bottom-origin", "options"),
    Output("travelers_opt2-board2-menu-top-year", "value"),
    Output("travelers_opt2-board2-menu-bottom-year", "value"),
    Output("travelers_opt2-board2-bottom-origin", "value"),
[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
])

def update_travelers_opt2_board1_menu(national_bt, international_bt):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt):
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt):
        category = "TURISTAS INTERNACIONALES"


    if category == "TURISTAS NACIONALES":
        menu_year = data.df_viajeros_nacional['AÑO'].unique()
        menu_origin = data.df_viajeros_nacional['ORIGEN'].unique()
    elif category == "TURISTAS INTERNACIONALES":
        menu_year = data.df_viajeros_internacional['AÑO'].unique()
        menu_origin = data.df_viajeros_internacional['ORIGEN'].unique()

    menu_year = list(map(layouts.create_options_dropdown, menu_year))
    menu_origin = list(map(layouts.create_options_dropdown, menu_origin))

    return menu_year, menu_year, menu_origin, \
        [menu_year[0]['value']], [menu_year[0]['value']], [menu_origin[0]['value']]



#Travelers -> OPT2 -> BOARD 2 -> attractions: GRAPH 1 (TOP lEFT)


#Travelers -> OPT2 -> BOARD 2 -> attractions: GRAPH 2 (TOP RIGHT)

#Travelers -> OPT2 -> BOARD 2 -> attractions: GRAPH 3 (BOTTOM)
@app.callback(
    Output("travelers_opt2-board2-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board2-menu-bottom-year", "value"),
    Input("travelers_opt2-board2-bottom-origin", "value"),
])
def update_travelers_travelers_opt2_b2_g3(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'ATRACTIVOS']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)

    fig = px.line(df_plot, x = "MES", y = "VIAJEROS", color = "ITEM", line_dash = 'ORIGEN',
                 color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                 category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                  labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'PURPOSE, ORIGIN','ORIGEN':''},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig

#------------------ BOARD 3 ----------------

#Travelers -> OPT2 -> BOARD 3 -> SPENDING: GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt2-board3-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board3-menu-top-year", "value"),
])
def update_travelers_travelers_opt2_b3_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    # selected_origin = [str(x) for x in selected_origin]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'GASTO DISTRI']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar_polar(df_plot,
                       r = 'VIAJEROS', theta = 'MES', color = 'ITEM',
                       barnorm = 'percent', template = 'plotly_white',
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'','ORIGEN':'ORIGIN'},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig


#Travelers -> OPT2 -> BOARD 3 -> SPENDING: GRAPH 2 (BOTTOM)

@app.callback(
    Output("travelers_opt2-board3-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board3-menu-bottom-year", "value"),
    Input("travelers_opt2-board3-bottom-origin", "value"),
])
def update_travelers_travelers_opt2_b3_g2(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'GASTO DISTRI']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)

    fig = px.line(df_plot, x = "MES", y = "VIAJEROS", color = "ITEM", line_dash = 'ORIGEN',
                 color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                 category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                  labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'','ORIGEN':'ORIGIN'},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig

#------------------ BOARD 4 ----------------

#Travelers -> OPT2 -> BOARD 4 -> GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt2-board4-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board4-menu-top-year", "value"),
])
def update_travelers_travelers_opt2_b4_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'GRUPO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar(df_plot,
                       x = 'MES', y = 'VIAJEROS', color = 'ITEM',
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'',},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig


#Travelers -> OPT2 -> BOARD 4 -> GRAPH 2 (BOTTOM)

@app.callback(
    Output("travelers_opt2-board4-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board4-menu-bottom-year", "value"),
    Input("travelers_opt2-board4-bottom-origin", "value"),
])
def update_travelers_travelers_opt2_b4_g2(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'GRUPO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)

    fig = px.line(df_plot, x = "MES", y = "VIAJEROS", color = "ITEM", line_dash = 'ORIGEN',
                 color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                 category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                  labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'','ORIGEN':'ORIGIN'},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig


#------------------ BOARD 5 ----------------

#Travelers -> OPT2 -> BOARD 5 -> GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt2-board5-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board5-menu-top-year", "value"),
])
def update_travelers_travelers_opt2_b5_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'ALOJAMIENTO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['ITEM']=='G. NS/NR'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar(df_plot,
                       x = 'MES', y = 'VIAJEROS', color = 'ITEM',
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'',},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig


#Travelers -> OPT2 -> BOARD 5 -> GRAPH 2 (BOTTOM)

@app.callback(
    Output("travelers_opt2-board5-graph-bottom", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board5-menu-bottom-year", "value"),
    Input("travelers_opt2-board5-bottom-origin", "value"),
])
def update_travelers_travelers_opt2_b5_g2(national_bt, international_bt, selected_year,selected_origin):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    selected_origin = [str(x) for x in selected_origin]

    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['ORIGEN'].isin(selected_origin)].loc[df_plot['SUBTEMA'] == 'ALOJAMIENTO']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)

    fig = px.line(df_plot, x = "MES", y = "VIAJEROS", color = "ITEM", line_dash = 'ORIGEN',
                 color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                 category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                  labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'','ORIGEN':'ORIGIN'},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig

#------------------ BOARD 6 ----------------

#Travelers -> OPT2 -> BOARD 6 -> GRAPH 1 (TOP)
@app.callback(
    Output("travelers_opt2-board6-graph-top", "figure")
,[
    Input("viajeros-selector-national", "n_clicks_timestamp"),
    Input("viajeros-selector-international", "n_clicks_timestamp"),
    
    Input("travelers_opt2-board6-menu-top-year", "value"),
])
def update_travelers_travelers_opt2_b6_g1(national_bt, international_bt, selected_year):
    # USING TYPE OF TOURIST FILTER
    category = "TURISTAS NACIONALES"
    if int(national_bt) > int(international_bt) :
        category = "TURISTAS NACIONALES"
    elif int(international_bt) > int(national_bt) :
        category = "TURISTAS INTERNACIONALES"


    #Creating the right graph
    if category == "TURISTAS NACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS NACIONALES"]
    elif category == "TURISTAS INTERNACIONALES":
        df_plot = data.df_viajeros[data.df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
    else:
        pass

    selected_year = [int(x) for x in selected_year]
    df_plot = df_plot.loc[df_plot['AÑO'].isin(selected_year)].loc[df_plot['SUBTEMA'] == 'Noches Pernoctadas']
    df_plot = df_plot.drop(index = df_plot.loc[df_plot['MES']=='TOTAL'].index)
    df_plot = df_plot.groupby(['MES','ITEM']).sum().reset_index()

    fig = px.bar(df_plot,
                       x = 'MES', y = 'VIAJEROS', color = 'ITEM',
                       color_discrete_sequence = COLOR_PALETTE_DISCRETE,
                       category_orders = {
                       "MES":['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE']},
                       labels = {'VIAJEROS':'TRAVELERS','MES':'MONTH',
                           'ITEM':'',},
            )
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO',
                              'AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'],
            ticktext = ['JAN','FEB','MAR','APR','MAY','JUN','JUL',
                              'AUG','SEP','OCT','NOV','DEC']
        )
    )
    return fig

#--------------------LAYOUT DECLARATION-------------------------

app.layout = index()



# Call app server
if __name__ == "__main__":
    # set debug to false when deploying app
    app.run_server(debug=True)
