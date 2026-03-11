#!/usr/bin/env python
# coding: utf-8

# In[1]:


# generate_pme_profiles.py
import pandas as pd
import numpy as np

np.random.seed(42)
n = 500
profiles = []

for _ in range(n):
    profiles.append({
        "statut_juridique": np.random.choice(["Auto-entrepreneur", "SARL", "Coopérative"]),
        "secteur_activite": np.random.choice(["Agriculture", "Tech", "Industrie", "Artisanat", "Tourisme"]),
        "taille": np.random.choice(["TPE", "PME", "Start-up"]),
        "region": np.random.choice(["Casablanca-Settat", "Rabat-Salé-Kénitra", "Souss-Massa", "Drâa-Tafilalet", "Fès-Meknès"]),
        "besoin_principal": np.random.choice(["Achat d'équipements", "Numérisation", "Export", "Formation", "Innovation"]),
        "annee_creation": np.random.randint(2020, 2025)
    })

df = pd.DataFrame(profiles)
df.to_csv("pme_profiles_test.csv", index=False)
print("Fichier créé: pme_profiles_test.csv")
print(df.head())


# In[ ]:




