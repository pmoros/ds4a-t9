import pandas as pd

# Plotly graph objects to render graph plots
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

#import requests
import json
import wrangler

# ------ Databases load -----------
databases = wrangler.read__file_databases()

df_viajeros = databases[wrangler.DATABASE_NAMES[0]]
df_indicadores_turismo = databases[wrangler.DATABASE_NAMES[1]]

# ------- Model related code -----------------------------------------

#----------Travelers-----------------------------------

#------Data sources-----
# geojson_col = requests.get("https://ds4a-team9-idt.s3.us-east-2.amazonaws.com/colombia.geojson")
# geojson_col = geojson_col.json()
col_path = "assets/colombia.geojson"
with open(col_path) as geo:
    geojson_col = json.loads(geo.read())


df_viajeros_nacional = df_viajeros[df_viajeros['TEMA'] == "TURISTAS NACIONALES"]

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
    zoom=4,
    featureidkey="properties.NOMBRE_DPT",
    mapbox_style="carto-positron",
    center={"lat": 4.1000, "lon": -72.9089},
    color_continuous_scale="Viridis",
    opacity=0.5, 
    title="National travelers by region"
    )
    
    return my_plot

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
df_gen_empleo_turismo["MES"] = df_gen_empleo_turismo['MES'].map(str)
df_gen_empleo_turismo["MES"] = df_gen_empleo_turismo["MES"].replace({"nan": ""})
df_gen_empleo_turismo['SUBTEMA2'] = df_gen_empleo_turismo['SUBTEMA'].map(str) + " " + df_gen_empleo_turismo['MES']
df_gen_empleo_turismo["SUBTEMA2"] = df_gen_empleo_turismo["SUBTEMA2"].replace({"Empleo Turismo Bogotá TRIM I": "Empleo Turismo Bogotá Trimestral"})
df_gen_empleo_turismo["SUBTEMA2"] = df_gen_empleo_turismo["SUBTEMA2"].replace({"Empleo Turismo Bogotá TRIM II": "Empleo Turismo Bogotá Trimestral"})
df_gen_empleo_turismo["SUBTEMA2"] = df_gen_empleo_turismo["SUBTEMA2"].replace({"Empleo Turismo Bogotá TRIM III": "Empleo Turismo Bogotá Trimestral"})
df_gen_empleo_turismo["SUBTEMA2"] = df_gen_empleo_turismo["SUBTEMA2"].replace({"Empleo Turismo Bogotá TRIM IV": "Empleo Turismo Bogotá Trimestral"})
df_gen_empleo_turismo['VALOR'] = df_gen_empleo_turismo['VALOR'].str.rstrip('%').astype(float)
df_gen_empleo_turismo = df_gen_empleo_turismo.drop(["TEMA","CLASE","FUENTE"], axis=1)

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
