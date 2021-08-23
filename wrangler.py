#Base de datos 2

def normalize_column_names_db2(df):
    
    df2 = df.copy()
    original_names = list(df2.columns)
    normalized_names = [x.upper() for x in original_names]
    
    df2.columns = normalized_names
    
    return df2
  
df_indicadores_turismo = pd.read_csv("2. Base de Indicadores de Turismo 2.csv")

df_indicadores_turismo = normalize_column_names_db2(df_indicadores_turismo)
