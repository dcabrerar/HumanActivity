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

