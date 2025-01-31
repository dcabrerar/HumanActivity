import streamlit as st
import pandas as pd
import numpy as np
import joblib
import asyncio
import websockets

# Interfaz de la aplicación
st.title('Detección de la actividad Humana en tiempo real')
st.write('Esta es una aplicación que recibe datos de sensores y predice la actividad en vivo')

# Botón para iniciar la conexión WebSocket
async def receive_data():
    async with websockets.connect('ws://190.43.25.106:8765') as websocket:
        while True:
            data = await websocket.recv()
            st.write(f'Actividad detectada: **{data}**')
            
if st.button('Iniciar Detección'):
    asyncio.run(receive_data())