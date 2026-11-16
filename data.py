import pandas as pd
import numpy as np
import plotly.express as px

# Plotly graph objects to render graph plots
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#import requests
import json
import datalayer
from datalayer.formatting import millify  # noqa: F401  (re-exported)


COLOR_PALETTE_DISCRETE = px.colors.qualitative.T10
COLOR_PALETTE_CONTINUOUS = "Darkmint"


COUNTRIES_ALPHA3 = {'ALEMANIA':"DEU", 'ARGENTINA':"ARG", 'BOLIVIA':"BOL", 'BRASIL':"BRA", 'CHILE':"CHL",
       'COSTA RICA':"CRI", 'ECUADOR':"ECU", 'ESPAÑA':"ESP", 'ESTADOS UNIDOS':"USA", 'FRANCIA':"FRA",
       'ITALIA':"ITA", 'MEXICO':"MEX", 'PANAMA':"PAN", 'PERU':"PER", 'REINO UNIDO':"GBR"}
    
CONTINENTS_ALPHA3 = {"DEU": "Europe","ARG": "Americas", "BOL": "Americas", "BRA": "Americas", "CHL": "Americas",
       "CRI": "Americas", "ECU": "Americas", "ESP": "Europe", "USA":"Americas", "FRA":"Europe",
       "ITA": "Europe", "MEX": "Americas", "PAN":"Americas", "PER":"Americas", "GBR":"Europe"}


# ------ Data (temporary aliases; callers move to datalayer next) -----------
df_viajeros = datalayer.travelers()
df_viajeros_nacional = datalayer.travelers(datalayer.TravelerKind.NATIONAL)
df_viajeros_internacional = datalayer.travelers(datalayer.TravelerKind.INTERNATIONAL)
df_indicadores_turismo = datalayer.indicators_raw()
geojson_col = datalayer.load_geojson()

df_airbnb_homeway = datalayer.indicator('airbnb_homeway')
df_bigdata = datalayer.indicator('bigdata')
df_cert_turismo_sostenible = datalayer.indicator('cert_turismo_sostenible')
df_conect_internacional = datalayer.indicator('conect_internacional')
df_gen_empleo_turismo = datalayer.indicator('gen_empleo_turismo')
df_gen_empleo_turismo2 = datalayer.indicator('gen_empleo_turismo2')
df_indice_competitividad_turistica = datalayer.indicator('indice_competitividad_turistica')
df_indice_presion_turistica = datalayer.indicator('indice_presion_turistica')
df_turismo_internacional = datalayer.indicator('turismo_internacional')
df_turismo_internacional2 = datalayer.indicator('turismo_internacional2')
df_pib = datalayer.indicator('pib')
df_prest_servicios_turisticos = datalayer.indicator('prest_servicios_turisticos')
df_prest_servicios_turisticos1 = datalayer.indicator('prest_servicios_turisticos1')
df_prest_servicios_turisticos2 = datalayer.indicator('prest_servicios_turisticos2')
df_tasa_ocupacion_airbnb = datalayer.indicator('tasa_ocupacion_airbnb')
df_tasa_ocupacion_hotelera = datalayer.indicator('tasa_ocupacion_hotelera')

#TRAVELERS -> OPT1 -> BOARD1 -> PLOT RIGHT
def viajeros_region_nacional_plot(years, months):
    global df_viajeros_nacional
    global geojson_col

    years = [int(x) for x in years]
    db_viajeros_nacional_filtered = df_viajeros_nacional[df_viajeros_nacional['AÑO'].isin(years)]
    db_viajeros_nacional_filtered = db_viajeros_nacional_filtered[db_viajeros_nacional_filtered['MES'].isin(months)]
    
    plot_data = db_viajeros_nacional_filtered.groupby('ORIGEN').sum().reset_index()
    

    
    my_plot = px.choropleth_mapbox(
    plot_data,
    locations="ORIGEN",
    color="VIAJEROS",
    geojson=geojson_col,
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
    global df_viajeros_internacional
    global COUNTRIES_ALPHA3

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
    df_plot = df_pib

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
    df_plot = df_indice_presion_turistica

    fig = px.line(df_plot, x='AÑO', y='VALOR',
             labels={
                'VALOR': "Value", 'AÑO': "Year"
            },
            color_discrete_sequence=COLOR_PALETTE_DISCRETE,
            )

    return fig    


#Main card functions (legacy signatures; flag 0: international, 1: national, other: both)
_FLAG_KIND = {0: datalayer.TravelerKind.INTERNATIONAL, 1: datalayer.TravelerKind.NATIONAL}


def prefCard(df, año, mes, flag):
    return datalayer.preference_card(año, mes, _FLAG_KIND.get(flag))


def travelCard(df, año, mes, flag):
    return datalayer.travel_card(año, mes, _FLAG_KIND.get(flag))
