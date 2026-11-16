import pandas as pd
import numpy as np
import plotly.express as px

# Plotly graph objects to render graph plots
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import datalayer


COLOR_PALETTE_DISCRETE = px.colors.qualitative.T10
COLOR_PALETTE_CONTINUOUS = "Darkmint"


COUNTRIES_ALPHA3 = {'ALEMANIA':"DEU", 'ARGENTINA':"ARG", 'BOLIVIA':"BOL", 'BRASIL':"BRA", 'CHILE':"CHL",
       'COSTA RICA':"CRI", 'ECUADOR':"ECU", 'ESPAÑA':"ESP", 'ESTADOS UNIDOS':"USA", 'FRANCIA':"FRA",
       'ITALIA':"ITA", 'MEXICO':"MEX", 'PANAMA':"PAN", 'PERU':"PER", 'REINO UNIDO':"GBR"}
    
CONTINENTS_ALPHA3 = {"DEU": "Europe","ARG": "Americas", "BOL": "Americas", "BRA": "Americas", "CHL": "Americas",
       "CRI": "Americas", "ECU": "Americas", "ESP": "Europe", "USA":"Americas", "FRA":"Europe",
       "ITA": "Europe", "MEX": "Americas", "PAN":"Americas", "PER":"Americas", "GBR":"Europe"}


#TRAVELERS -> OPT1 -> BOARD1 -> PLOT RIGHT
def viajeros_region_nacional_plot(years, months):
    df_viajeros_nacional = datalayer.travelers(datalayer.TravelerKind.NATIONAL)

    years = [int(x) for x in years]
    db_viajeros_nacional_filtered = df_viajeros_nacional[df_viajeros_nacional['AÑO'].isin(years)]
    db_viajeros_nacional_filtered = db_viajeros_nacional_filtered[db_viajeros_nacional_filtered['MES'].isin(months)]
    
    plot_data = db_viajeros_nacional_filtered.groupby('ORIGEN').sum().reset_index()
    

    
    my_plot = px.choropleth_mapbox(
    plot_data,
    locations="ORIGEN",
    color="VIAJEROS",
    geojson=datalayer.load_geojson(),
    zoom=4.1,
    featureidkey="properties.NOMBRE_DPT",
    mapbox_style="carto-positron",
    #center={"lat": 4.1000, "lon": -72.9089},
    center={"lat": 4.824335, "lon": -74.063644},
    color_continuous_scale="Viridis",
    #color_continuous_scale="deep",
    opacity=0.5, 
    #Title would be in the left plot
    #title="National travelers by region"
    )
    
    return my_plot


def viajeros_region_internacional_plot(years, months):
    df_viajeros_internacional = datalayer.travelers(datalayer.TravelerKind.INTERNATIONAL)

    years = [int(x) for x in years]
    db_viajeros_internacional_filtered = df_viajeros_internacional[df_viajeros_internacional['AÑO'].isin(years)]
    db_viajeros_internacional_filtered = db_viajeros_internacional_filtered[db_viajeros_internacional_filtered['MES'].isin(months)]
    
    plot_data = db_viajeros_internacional_filtered.groupby('ORIGEN').sum().reset_index()    
    plot_data['iso_alpha'] = plot_data['ORIGEN'].replace(COUNTRIES_ALPHA3)
    plot_data['Continent'] = plot_data['iso_alpha'].replace(CONTINENTS_ALPHA3)
    
    fig = px.scatter_geo(plot_data, locations="iso_alpha", color="Continent",
                     hover_name="ORIGEN", size="VIAJEROS",
                     projection="natural earth")    
    
    
    return fig
    

#-----------Static graphs (figures) ------------
def get_indicators_opt3_b1_g1():
    df_plot = datalayer.indicator('pib')

    fig = px.line(df_plot, x='AÑO', y='VALOR', color='CLASE', line_group='CLASE',
             category_orders={"CLASE":["Subsector: Alojamiento y comida","Sector: Alojamiento y comida"]},
             labels={
                'VALOR': "GDP (%)", 'AÑO': "Year", 'CLASE': ""
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )
    fig.update_traces(mode='markers+lines')

    return fig


#Indicators-> SIGHTSEEING -> BOARD 4 -> GRAPH 1
def get_indicators_opt4_b4_g1():
    df_plot = datalayer.indicator('indice_presion_turistica')

    fig = px.line(df_plot, x='AÑO', y='VALOR',
             labels={
                'VALOR': "Value", 'AÑO': "Year"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )

    return fig
