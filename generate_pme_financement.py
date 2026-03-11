#!/usr/bin/env python
# coding: utf-8

# In[3]:


# generate_pme_financement.py
import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
    "statut_juridique": np.random.choice(["Auto-entrepreneur", "Personne physique", "Coopérative"], n),
    "secteur_activite": np.random.choice(["Agriculture", "Tourisme", "Tech", "Artisanat", "Commerce", "Industrie"], n),
    "taille": np.random.choice(["TPE", "PME", "Start-up"], n),
    "region": np.random.choice(["Casablanca-Settat", "Rabat-Salé-Kénitra", "Marrakech-Safi", "Fès-Meknès", "Tanger-Tétouan", "Autre"], n)
}

df = pd.DataFrame(data)

def generer_montant(row):
    base = 50000
    if row["taille"] == "PME":
        base *= 3
    elif row["taille"] == "Start-up":
        base *= 5
    if row["secteur_activite"] in ["Tech", "Industrie"]:
        base *= 1.5
    elif row["secteur_activite"] == "Agriculture":
        base *= 0.8
    if row["statut_juridique"] == "Coopérative":
        base *= 1.2
    if row["region"] == "Casablanca-Settat":
        base *= 1.3
    return int(base * np.random.uniform(0.8, 1.2))

df["montant_financement"] = df.apply(generer_montant, axis=1)
df.to_csv("pme_financement_maroc.csv", index=False)
print("Fichier créé: pme_financement_maroc.csv")
print(df.head())


# In[ ]:




