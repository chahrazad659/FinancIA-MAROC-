# app_streamlit.py
import streamlit as st
import pandas as pd
import json

st.title("FinancIA-MAROC - Recommandation Subventions")

uploaded_file = st.file_uploader("Téléchargez le profil PME (CSV)")
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='utf-8')
    st.write("Profil PME:")
    st.dataframe(df)

    with open("subventions_maroc.json", encoding='utf-8') as f:
        subventions = json.load(f)

    st.write("Subventions possibles pour la première PME:")
    first_pme = df.iloc[0].to_dict()
    
    for s in subventions:
        conditions = s.get("conditions", {})
        secteur_ok = first_pme["secteur_activite"] in conditions.get("secteurs", [])
        taille_ok = first_pme["taille"] in conditions.get("tailles", [])
        region_ok = first_pme["region"] in conditions.get("regions", [])
        statut_ok = first_pme.get("statut_juridique") in conditions.get("statuts", [first_pme.get("statut_juridique")])
        if secteur_ok and taille_ok and region_ok and statut_ok:
            st.write(f"- {s['nom']} ({s['organisme']}): {s['description']}")