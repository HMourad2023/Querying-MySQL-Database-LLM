import mysql.connector
from mysql.connector import Error
import os
import pandas as pd

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if connection.is_connected():
            print("Connection réussie !")
            return connection
        else:
            print("Échec de la connexion.")
            return None

    except Error as e:
        print(f"Erreur: {e}")
        return None

def fetch_data_from_sql(query, connection):
    
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df

