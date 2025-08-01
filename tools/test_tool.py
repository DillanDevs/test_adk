import json
import random
from datetime import datetime

def get_weather_info(city: str, country: str = ""):
    """
    Obtiene información del clima para una ciudad específica.
    
    Args:
        city (str): Nombre de la ciudad
        country (str): País (opcional)
    
    Returns:
        dict: Información del clima simulada
    """
    # Simulamos datos de clima para fines de demostración
    weather_conditions = ["soleado", "parcialmente nublado", "nublado", "lluvioso", "tormentoso"]
    temperatures = list(range(15, 35))  # Temperaturas entre 15-35°C
    humidity_levels = list(range(40, 90))  # Humedad entre 40-90%
    
    # Generamos datos simulados
    current_weather = {
        "ciudad": city,
        "pais": country if country else "No especificado",
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperatura": random.choice(temperatures),
        "condicion": random.choice(weather_conditions),
        "humedad": random.choice(humidity_levels),
        "viento_kmh": random.randint(5, 25),
        "sensacion_termica": random.choice(temperatures) + random.randint(-3, 3)
    }
    
    return json.dumps(current_weather, ensure_ascii=False, indent=2)

def get_weather_forecast(city: str, days: int = 3):
    """
    Obtiene el pronóstico del clima para los próximos días.
    
    Args:
        city (str): Nombre de la ciudad
        days (int): Número de días para el pronóstico (máximo 7)
    
    Returns:
        dict: Pronóstico del clima simulado
    """
    if days > 7:
        days = 7
    
    weather_conditions = ["soleado", "parcialmente nublado", "nublado", "lluvioso", "tormentoso"]
    forecast = []
    
    for day in range(days):
        day_forecast = {
            "dia": day + 1,
            "fecha": datetime.now().strftime(f"%Y-%m-%{datetime.now().day + day + 1:02d}"),
            "temperatura_max": random.randint(20, 35),
            "temperatura_min": random.randint(10, 20),
            "condicion": random.choice(weather_conditions),
            "probabilidad_lluvia": random.randint(0, 100)
        }
        forecast.append(day_forecast)
    
    result = {
        "ciudad": city,
        "pronostico": forecast
    }
    
    return json.dumps(result, ensure_ascii=False, indent=2)