import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargamos el modelo entrenado
model = joblib.load('human_activity_model.pkl')

# Función para predecir la actividad
def predict_activity(data):
    # El modelo espera un array 2d (n_samples, n_features)
    prediction=model.predict(data)
    return prediction[0]

# Interfaz de la aplicación
st.title('Predicción de actividad humana')
st.write('Este es un ejemplo de cómo predecir la actividad humana a partir de datos de acelerómetro')

# Simulación de entrada en tiempo real
st.sidebar.title('Entradas del sensor')
tBodyAcc_mean_X = st.sidebar.slider('tBodyAcc-mean()-X', -1.0, 1.0, 0.0, 0.01)
tBodyAcc_mean_y = st.sidebar.slider('tBodyAcc-mean()-Y', -1.0, 1.0, 0.0, 0.01)
tBodyAcc_mean_Z = st.sidebar.slider('tBodyAcc-mean()-Z', -1.0, 1.0, 0.0, 0.01)

# Construimos un array 2d con los datos de entrada
input_data = np.array([[tBodyAcc_mean_X, tBodyAcc_mean_y, tBodyAcc_mean_Z]])

# Realizamos la predicción
if st.button('Predecir actividad'):
    activity = predict_activity(input_data)
    st.write('La actividad humana predicha es:',activity)