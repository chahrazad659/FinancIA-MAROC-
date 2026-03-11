#!/usr/bin/env python
# coding: utf-8

# In[2]:


# train_random_forest.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("pme_financement_maroc.csv")

X = df[["statut_juridique","secteur_activite","taille","region"]]
y = df["montant_financement"]

encoder = OneHotEncoder(drop='first', sparse_output=False)
X_encoded = encoder.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MAE: {mae:,.0f} MAD")
print(f"R²: {r2:.2f}")

feature_names = encoder.get_feature_names_out(X.columns)
importances = model.feature_importances_
indices = np.argsort(importances)[::-1][:5]
print("Top 5 features influentes:")
for i in indices:
    print(f"{feature_names[i]}: {importances[i]:.3f}")


# In[ ]:




