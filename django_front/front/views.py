"""Vistas para la app front."""
from __future__ import annotations

import json
import os
from pathlib import Path

import numpy as np
import tensorflow as tf
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Cargar el modelo H5
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODEL_PATH = BASE_DIR / "modelo_celsius_fahrenheit.h5"

# Variable global para el modelo
modelo = None

def cargar_modelo():
    """Carga el modelo la primera vez que se necesita."""
    global modelo
    if modelo is None:
        modelo = tf.keras.models.load_model(str(MODEL_PATH))
    return modelo


def home(request):
    """Renderiza la página principal con el front de inferencia."""
    return render(request, "front/index.html")


@csrf_exempt
def predict(request):
    """API endpoint para realizar predicciones con el modelo."""
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido. Use POST."}, status=405)
    
    try:
        data = json.loads(request.body)
        celsius = float(data.get("celsius", 0))
        
        model = cargar_modelo()
        
        input_data = np.array([[celsius]], dtype=np.float32)
        
        prediccion = model.predict(input_data, verbose=0)
        fahrenheit = float(prediccion[0][0])
        
        return JsonResponse({
            "celsius": celsius,
            "fahrenheit": fahrenheit,
            "success": True
        })
    
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error completo:\n{error_detail}")
        
        return JsonResponse({
            "error": f"Error en la predicción: {str(e)}",
            "success": False
        }, status=400)


