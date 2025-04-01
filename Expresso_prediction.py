import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Charger le modèle sauvegardé
model = joblib.load("rf_model.pkl")  

# Titre de l'application
st.title("Application de Prédictions avec Streamlit")

# Interface utilisateur dynamique pour entrer les caractéristiques
st.subheader("Entrez les caractéristiques ou variables d'entrée :")
num_features = st.slider("Nombre de features :", min_value=1, max_value=13, value=3)  # Slider pour définir le nombre de features

st.subheader("Entrez les valeurs pour chaque caractéristique")

Titles=['MONTANT', 'FREQUENCE_RECH', 'REVENUE', 'ARPU_SEGMENT', 'FREQUENCE', 'DATA_VOLUME', 'ON_NET', 'ORANGE', 'TIGO', 'MRG', 'REGULARITY', 'TOP_PACK', 'FREQ_TOP_PACK']
input_data = []  # Liste pour stocker les entrées utilisateur
for title in Titles:
    feature = st.number_input(f"{title} :", min_value=0.0, max_value=50000.0)
    input_data.append(feature)


# Bouton pour effectuer la prédiction
if st.button("Prédire"):    
    input_array = np.array([input_data])  # Convertir en tableau numpy    
    prediction = model.predict(input_array)     
    st.success(f"Prédiction : {prediction[0]}")    

if st.button('Effacer les données'):
    st.rerun()  # Recharger l'application pour effacer les données
    st.write("Données effacées.")

