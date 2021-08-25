import os
import pandas as pd

# -------------- Data cleaning related code ------- 

DATA_DIRECTORY = "data"

DATABASE_NAMES = ["base_viajeros", "base_indicadores"]


def clean_database_viajeros():    
    '''
        Wrangles the misspelling, repeated values, etc.

        return:
            df_cleaned: cleaned data frame ready to use.        
    '''
    # Sample code for reading the database file/s
    db_name = DATABASE_NAMES[0]
    database_path = os.path.join(DATA_DIRECTORY, db_name)

    df_database = pd.read_excel(database_path)
    #--> Code for cleaning the database

    #--> End of code for cleaning the database

    df_cleaned = df_database # Assign the result from the cleaning operation

    return df_cleaned

def clean_database_indicadores():
    '''
        Wrangles the misspelling, repeated values, etc.

        return:
            df_cleaned: cleaned data frame ready to use.        
    '''
    db_name = DATABASE_NAMES[1]
    database_path = os.path.join(DATA_DIRECTORY, db_name)

    df_database = pd.read_excel(database_path)
    #--> Code for cleaning the database

    #--> End of code for cleaning the database

    df_cleaned = df_database # Assign the result from the cleaning operation

    return df_cleaned


def read__file_databases():
    '''Automatically loads the databases from the csv files
        return:
            databases: dictionary with the cleaned dataframes
            DATABASE_NAMES can be used to access each one.
    '''
    databases = {}
    databases[DATABASE_NAMES[0]] = clean_database_viajeros()
    databases[DATABASE_NAMES[1]] = clean_database_indicadores()

    return databases


# ---------------- Relational database related code --------

def create_relational_db():
    '''This contains the code necessary for the creation of 
       the tables and users.'''
    pass

def upload__datasets():
    '''
        Loads the cleaned databases into a PostgreSQL database.

        return:
            operation_result
    '''
    pass

