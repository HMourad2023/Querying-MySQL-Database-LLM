import streamlit as st
from PIL import Image
from src.config import load_env, load_params
from src.database import connect_to_mysql, fetch_data_from_sql
from src.query import query_data
from src.utils import dataframe_to_json
from src.generate import generate_pdf,generate_pdf_and_save
import os

import pytz
from datetime import datetime

load_env()
params = load_params()

def main():
    # Chargement des paramètres depuis params.yaml
    model_names = params['model_names']
    default_model = params['default_model']
    num_records_default = params['num_records']

    # Interface Streamlit
    st.title("MySQL Querying with Groq")
    image = Image.open('images/image1.png')
    st.image(image, use_container_width=True)
    # Get the current datetime with the EST timezone
    current_time = datetime.now(pytz.timezone("US/Eastern"))

    # Format the datetime to show only the date and time (hour and minute)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M")

    # Display the formatted datetime in the center using Markdown
    st.markdown(f"<h2 style='text-align: center;'>{formatted_time}</h2>", unsafe_allow_html=True)

    # Sidebar pour la configuration de la connexion
    with st.sidebar.expander("Connection and Query Settings"):
        username = st.text_input("MYSQL", value=os.getenv("DB_USER"))
        password = st.text_input("Password", value=os.getenv("DB_PASSWORD"), type="password")
        host = st.text_input("Host", value=os.getenv("DB_HOST"))
        port = st.text_input("Port", value=os.getenv("DB_PORT"))
        database = st.text_input("Database", value=os.getenv("DB_NAME"))

        # Connexion à MySQL et récupération des aéroports
        conn = connect_to_mysql()
        names_query = "SELECT DISTINCT airport FROM airline_delay"
        airport_names_df = fetch_data_from_sql(names_query, conn)
        airport_names = airport_names_df['airport'].tolist()

        # Sélection multiple d'aéroports
        selected_names = st.multiselect("Select Airport", airport_names)

        # Requête SQL de base
        base_query = "SELECT * FROM airline_delay"
        
        # Modification de la requête en fonction des aéroports sélectionnés
        if selected_names:
            airports_filter = ", ".join(f"'{name}'" for name in selected_names)
            query = f"{base_query} WHERE airport IN ({airports_filter})"
        else:
            query = base_query

        # Sélection du nombre de records à afficher
        num_records = st.slider("Select Number of Records to Display", min_value=10, max_value= 300, value=num_records_default)

        # Saisie de la question
        question = st.text_area("Ask a Question", value="Write a summary of our data")

        # Sélection du modèle
        model_name = st.selectbox("Select Model", model_names, index=model_names.index(default_model))

        # API Key
        api_key = os.getenv("GROQ_API_KEY")

    if st.button("Fetch and Query Data"):
        if api_key and username and port and host and password and database and query and question:
            try:
                # Connexion à MySQL et récupération des données
                conn = connect_to_mysql()
                df = fetch_data_from_sql(query, conn)

                # Limiter les données en fonction de la sélection de l'utilisateur
                limited_data = df.head(num_records)

                # Conversion en JSON
                data_json = dataframe_to_json(limited_data)

                # Interroger Groq
                answer = query_data(data_json, question, model_name, api_key)

                # Affichage de la réponse
                st.subheader("Answer:")
                st.write(answer)
                saved_pdf_path = generate_pdf_and_save(answer)

                if saved_pdf_path:
                    print(f"Le PDF a été sauvegardé avec succès à : {saved_pdf_path}")
                else:
                    print("Une erreur est survenue lors de la génération du PDF.")

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please fill in all the fields.")

if __name__ == "__main__":
    main()
