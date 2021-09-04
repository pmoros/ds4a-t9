import pandas as pd
import plotly.express as px

# Plotly graph objects to render graph plots
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#import requests
import json
import wrangler


COLOR_PALETTE_DISCRETE = px.colors.qualitative.T10
COLOR_PALETTE_CONTINUOUS = "Darkmint"


COUNTRIES_ALPHA3 = {'ALEMANIA':"DEU", 'ARGENTINA':"ARG", 'BOLIVIA':"BOL", 'BRASIL':"BRA", 'CHILE':"CHL",
       'COSTA RICA':"CRI", 'ECUADOR':"ECU", 'ESPAÑA':"ESP", 'ESTADOS UNIDOS':"USA", 'FRANCIA':"FRA",
       'ITALIA':"ITA", 'MEXICO':"MEX", 'PANAMA':"PAN", 'PERU':"PER", 'REINO UNIDO':"GBR"}
    
CONTINENTS_ALPHA3 = {"DEU": "Europe","ARG": "Americas", "BOL": "Americas", "BRA": "Americas", "CHL": "Americas",
       "CRI": "Americas", "ECU": "Americas", "ESP": "Europe", "USA":"Americas", "FRA":"Europe",
       "ITA": "Europe", "MEX": "Americas", "PAN":"Americas", "PER":"Americas", "GBR":"Europe"}


# ------ Databases load -----------
databases = wrangler.read__file_databases()

df_viajeros = databases[wrangler.DATABASE_NAMES[0]]
df_indicadores_turismo = databases[wrangler.DATABASE_NAMES[1]]

#----------Travelers-----------------------------------

#------Data sources-----
# geojson_col = requests.get("https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/colombia.geojson")
# geojson_col = geojson_col.json()
col_path = "assets/colombia.geojson"
with open(col_path) as geo:
    geojson_col = json.loads(geo.read())


df_viajeros_nacional = df_viajeros[df_viajeros['TEMA'] == "TURISTAS NACIONALES"]



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


df_viajeros_internacional = df_viajeros[df_viajeros['TEMA'] == "TURISTAS INTERNACIONALES"]
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
    

#----------Indicators----------------------------------

#----------Airbnb & Homeaway----------

df_airbnb_homeway = df_indicadores_turismo.copy()
df_airbnb_homeway = df_airbnb_homeway[df_airbnb_homeway["TEMA"] == "Airbnb & Homeaway"]
df_airbnb_homeway = df_airbnb_homeway.drop(["TEMA","VARIABLE","CLASE","FUENTE","MES"], axis=1)
df_airbnb_homeway['VALOR'] = df_airbnb_homeway['VALOR'].astype(float)

#----------Big Data----------

df_bigdata = df_indicadores_turismo.copy()
df_bigdata = df_bigdata[df_bigdata["TEMA"] == "Big Data"]
df_bigdata['VALOR'] = df_bigdata['VALOR'].astype(float)
df_bigdata = df_bigdata.drop(["TEMA","FUENTE","MES"], axis=1)

#----------Certificación de Turismo Sostenible----------

df_cert_turismo_sostenible = df_indicadores_turismo.copy()
df_cert_turismo_sostenible = df_cert_turismo_sostenible[df_cert_turismo_sostenible["TEMA"] == "Certificación de Turismo Sostenible"]
df_cert_turismo_sostenible['VALOR'] = df_cert_turismo_sostenible['VALOR'].astype(float)
df_cert_turismo_sostenible = df_cert_turismo_sostenible.drop(["TEMA","FUENTE","MES"], axis=1)
df_cert_turismo_sostenible = df_cert_turismo_sostenible.replace({"Sedes para eventos, congresos, ferias y convenciones": "Sedes para eventos"})
df_cert_turismo_sostenible = df_cert_turismo_sostenible.replace({"Establecimientos gastronómicos y bares": "Establecimientos gastronómicos"})

#----------Conectividad directa internacional----------

df_conect_internacional = df_indicadores_turismo.copy()
df_conect_internacional = df_conect_internacional[df_conect_internacional["TEMA"] == "Conectividad directa internacional"]
df_conect_internacional['VALOR'] = df_conect_internacional['VALOR'].astype(float)
df_conect_internacional = df_conect_internacional.drop(["TEMA","CLASE","FUENTE","MES"], axis=1)

#----------Generación de empleo turismo----------

df_gen_empleo_turismo = df_indicadores_turismo.copy()
df_gen_empleo_turismo = df_gen_empleo_turismo[df_gen_empleo_turismo["TEMA"] == "Generación de empleo turismo"]
df_gen_empleo_turismo = df_gen_empleo_turismo.drop(["TEMA","CLASE","FUENTE"], axis=1)
df_gen_empleo_turismo['VALOR'] = df_gen_empleo_turismo['VALOR'].str.rstrip('%').astype(float)

df_gen_empleo_turismo2 = df_gen_empleo_turismo[df_gen_empleo_turismo["MES"].notnull()]

df_gen_empleo_turismo = df_gen_empleo_turismo[df_gen_empleo_turismo["MES"].isnull()]

#----------Índice de Competitividad Turística Regional----------

df_indice_competitividad_turistica = df_indicadores_turismo.copy()
df_indice_competitividad_turistica = df_indice_competitividad_turistica[df_indice_competitividad_turistica["TEMA"] == "Índice de Competitividad Turística Regional de Colombia-ICTRC"]
df_indice_competitividad_turistica['VALOR'] = df_indice_competitividad_turistica['VALOR'].astype(float)
df_indice_competitividad_turistica = df_indice_competitividad_turistica.drop(["TEMA","CLASE","FUENTE","MES"], axis=1)

#----------Índice de Presión Turística----------

df_indice_presion_turistica = df_indicadores_turismo.copy()
df_indice_presion_turistica = df_indice_presion_turistica[df_indice_presion_turistica["TEMA"] == "Índice de Presión Turística"]
df_indice_presion_turistica['VALOR'] = df_indice_presion_turistica['VALOR'].astype(float)
df_indice_presion_turistica = df_indice_presion_turistica.drop(["TEMA","SUBTEMA","VARIABLE","CLASE","FUENTE","MES"], axis=1)

#----------Informacion Destacada del turismo internacional----------

df_turismo_internacional = df_indicadores_turismo.copy()
df_turismo_internacional = df_turismo_internacional[df_turismo_internacional["TEMA"] == "Informacion Destacada del turismo internacional"]
values = ["Exportaciones Totales de Turismo Internacional","Ingresos por turismo internacional","Llegadas de Turistas Internacionales","Transporte Internacional de Pasajeros"]
df_turismo_internacional = df_turismo_internacional[df_turismo_internacional["VARIABLE"].isin(values)]
df_turismo_internacional['VALOR'] = df_turismo_internacional['VALOR'].astype(float)
df_turismo_internacional = df_turismo_internacional.drop(["TEMA","FUENTE","MES"], axis=1)

df_turismo_internacional2 = df_indicadores_turismo.copy()
df_turismo_internacional2 = df_turismo_internacional2[df_turismo_internacional2["TEMA"] == "Informacion Destacada del turismo internacional"]
values = ["Proposito del Viaje","Medio de Transporte"]
df_turismo_internacional2 = df_turismo_internacional2[df_turismo_internacional2["VARIABLE"].isin(values)]
df_turismo_internacional2['VALOR'] = df_turismo_internacional2['VALOR'].str.rstrip('%').astype(float)
df_turismo_internacional2 = df_turismo_internacional2.drop(["TEMA","FUENTE","MES"], axis=1)

#----------PIB----------

df_pib = df_indicadores_turismo.copy()
df_pib = df_pib[df_pib["TEMA"] == "PIB"]
df_pib = df_pib.drop(["TEMA","SUBTEMA","VARIABLE","FUENTE","MES"], axis=1)
df_pib = df_pib.replace({"Sector: Comercio al por mayor y al por menor; reparación de vehículos automotores y motocicletas; Transporte y almacenamiento; Alojamiento y servicios de comida/ PIB Bogotá": "Sector: Alojamiento y comida"})
df_pib = df_pib.replace({"Subsector: Alojamiento y servicio de comida/ PIB Bogotá": "Subsector: Alojamiento y comida"})

#----------Prestadores de Servicios Turísticos----------

df_prest_servicios_turisticos = df_indicadores_turismo.copy()
df_prest_servicios_turisticos = df_prest_servicios_turisticos[df_prest_servicios_turisticos["TEMA"] == "Prestadores de Servicios Turísticos - PST"]
df_prest_servicios_turisticos = df_prest_servicios_turisticos[df_prest_servicios_turisticos["VARIABLE"] == "Total"]
df_prest_servicios_turisticos['VALOR'] = df_prest_servicios_turisticos['VALOR'].astype(float)
df_prest_servicios_turisticos = df_prest_servicios_turisticos.drop(["TEMA","CLASE","FUENTE","MES","VARIABLE"], axis=1)
df_prest_servicios_turisticos = df_prest_servicios_turisticos.replace({"Establecimiento de gastronomia y similares": "Establecimiento gastronomico"})
df_prest_servicios_turisticos = df_prest_servicios_turisticos.replace({"Establecimiento de alojamiento y hospedaje": "Alojamiento"})
df_prest_servicios_turisticos = df_prest_servicios_turisticos.replace({"Arrendadores de vehiculos para turismo nacional e internacional": "Arrendadores de vehiculos"})
df_prest_servicios_turisticos = df_prest_servicios_turisticos.replace({"Empresas captadoras de ahorro para viajes y de servicios turisticos": "Empresas captadoras de ahorro para servicios turisticos"})
df_prest_servicios_turisticos = df_prest_servicios_turisticos.replace({"Usuarios operadores, desarrolladores e industriales en zonas francas turísticas": "Usuarios operadores en zonas francas turísticas"})
df_prest_servicios_turisticos1 = df_prest_servicios_turisticos.query("VALOR>400") 
df_prest_servicios_turisticos2 = df_prest_servicios_turisticos.query("VALOR<400")

#----------Tasa de ocupación Airbnb----------

df_tasa_ocupacion_airbnb = df_indicadores_turismo.copy()
df_tasa_ocupacion_airbnb = df_tasa_ocupacion_airbnb[df_tasa_ocupacion_airbnb["TEMA"] == "Tasa de ocupación Airbnb"]
df_tasa_ocupacion_airbnb = df_tasa_ocupacion_airbnb.drop(["TEMA","VARIABLE","CLASE","FUENTE"], axis=1)
df_tasa_ocupacion_airbnb['AÑO-MES'] = df_tasa_ocupacion_airbnb['AÑO'].map(str) + "-" + df_tasa_ocupacion_airbnb['MES']
df_tasa_ocupacion_airbnb['MES'] = pd.to_numeric(df_tasa_ocupacion_airbnb['MES'])
df_tasa_ocupacion_airbnb = df_tasa_ocupacion_airbnb.query("MES>0") 
df_tasa_ocupacion_airbnb['VALOR'] = df_tasa_ocupacion_airbnb['VALOR'].str.rstrip('%').astype(float)

#----------Tasa de ocupación Hotelera----------

df_tasa_ocupacion_hotelera = df_indicadores_turismo.copy()
df_tasa_ocupacion_hotelera = df_tasa_ocupacion_hotelera[df_tasa_ocupacion_hotelera["TEMA"] == "Tasa de ocupación Hotelera"]
df_tasa_ocupacion_hotelera = df_tasa_ocupacion_hotelera.drop(["TEMA","VARIABLE","CLASE","FUENTE"], axis=1)
df_tasa_ocupacion_hotelera['MES'] = df_tasa_ocupacion_hotelera['MES'].map(str)
df_tasa_ocupacion_hotelera = df_tasa_ocupacion_hotelera.query("MES!='nan'")
df_tasa_ocupacion_hotelera['AÑO-MES'] = df_tasa_ocupacion_hotelera['AÑO'].map(str) + "-" + df_tasa_ocupacion_hotelera['MES']
df_tasa_ocupacion_hotelera['VALOR'] = df_tasa_ocupacion_hotelera['VALOR'].str.rstrip('%').astype(float)


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