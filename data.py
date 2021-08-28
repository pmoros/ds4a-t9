import wrangler
# ------ Databases load -----------
databases = wrangler.read__file_databases()

df_viajeros = databases[wrangler.DATABASE_NAMES[0]]
df_indicadores = databases[wrangler.DATABASE_NAMES[0]]
# ------- Lists for the selectors --------

# All the variables that end in _list will be used as
# lists for the frontend selectors

# viajeros_tema_list = df_viajeros['TEMA']

viajeros_tema_list = {}
viajeros_tema_list["INTERNATIONAL"] = "TURISTAS INTERNACIONALES"
viajeros_tema_list["NATIONAL"] = "TURISTAS INTERNACIONALES"
viajeros_tema_list["BOTH"] = "BOTH"

# ------- Model related code -------------
