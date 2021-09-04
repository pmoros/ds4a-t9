

import os
import pandas as pd

# -------------- Data cleaning related code -------

DATA_DIRECTORY = "data"

DATABASE_NAMES = ["base_viajeros.xlsx", "base_indicadores"]
GEOJSON_FILES = ["colombia.geojson"]

def clean_database_travelers():
    '''
        Wrangles the misspelling, repeated values, etc.

        return:
            df_cleaned: cleaned data frame ready to use.        
    '''
    # Sample code for reading the database file/s
    db_name = DATABASE_NAMES[0]
    database_path = os.path.join(DATA_DIRECTORY, db_name)

    df_database = pd.read_excel(database_path)
    # --> Code for cleaning the database

    # --> End of code for cleaning the database

    df_cleaned = df_database  # Assign the result from the cleaning operation

    return df_cleaned


def clean_database_indicators():
    '''
        Wrangles the misspelling, repeated values, etc.

        return:
            df_cleaned: cleaned data frame ready to use.        
    '''

    df = pd.read_csv("data/2. Base de Indicadores de Turismo 2.csv")
    
    original_names = list(df.columns)
    df.columns= [x.upper() for x in original_names]
    df_cleaned = df

    return df_cleaned


def read__file_databases():
    '''Automatically loads the databases from the csv files
        return:
            databases: dictionary with the cleaned dataframes
            DATABASE_NAMES can be used to access each one.
    '''
    databases = {}
    databases[DATABASE_NAMES[0]] = clean_database_travelers()
    databases[DATABASE_NAMES[1]] = clean_database_indicators()

    return databases


