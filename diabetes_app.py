# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Título de la aplicación
st.title("CONSULTE AQUÍ SI PADECE DE DIABETES")

st.write("Tener en cuenta que los valores de 1 indican la presencia de diabetes y 0 indica la ausencia de diabetes")

# Cargar dataframe
import os
archivo_csv = os.path.join(os.getcwd(), 'Data_preparada_Diabetes.csv')

# Leer el archivo CSV
df = pd.read_csv(archivo_csv)


y=df.Diabetes
X=df.drop('Diabetes',axis=1)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión logística
model = LogisticRegression()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones en los datos de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Mostrar la precisión en la aplicación

st.write(f"Exactitud del modelo: {accuracy*100:.2f}%")

# Agregar un input para que el usuario pueda ingresar nuevos datos
st.header("PREDECIR CON NUEVOS DATOS")
feature1 = st.number_input("EDAD", value=49,step=1)
feature2 = st.number_input("HIPERTENSION ( Tiene valores de 0 o 1, donde 0 indica que no se tiene hipertensión y 1 significa que se tiene hipertensión.)", value=0,step=1)
feature3 = st.number_input("CARDIOPATIA (Tiene valores de 0 o 1, donde 0 indica que no tiene enfermedad cardíaca y 1 significa que tiene enfermedad cardíaca.)", value=0,step=1)
feature4 = st.number_input("NIVEL HEMOGLOBINA (Normalmente oscila entre 3.5 y 9)", value=0.0, format="%.1f",step=0.1)
feature5 = st.number_input("NIVEL GLUCOSA EN SANGRE (Normalmente oscila entre 80 y 300)", value=0,step=1)



# Crear un botón para realizar la predicción
if st.button("CONSULTE SU ESTADO"):
  new_data = np.array([[feature1, feature2,feature3,feature4,feature5]])
  prediction = model.predict(new_data)[0]
  st.write(f"Predicción: {prediction}")
