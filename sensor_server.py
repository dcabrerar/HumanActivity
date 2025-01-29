import asyncio
import websockets
import numpy as np
import joblib

# Cargamos el modelo entrenado
model=joblib.load('human_activity_model.pkl')

# Función para predecir la actividad
def predict_activity(data):
    data=np.array(data).reshape(1,-1) # Ajuste de dimensiones
    prediction=model.predict(data)
    return prediction[0]

# Función para manejar la conexión
async def server(websocket, path):
    async for message in websocket:
        try:
            # Convertir los datos del sensor en una lista de floats
            sensor_data=list(map(float,message.split(',')))
            
            # Realizar la predicción
            activity=predict_activity(sensor_data)
            
            # Enviar la predicción al cliente
            await websocket.send(str(activity))
            
        except Exception as e:
            await websocket.send('Error: '+str(e))
            
# Iniciar el servidor WebSocket
start_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()