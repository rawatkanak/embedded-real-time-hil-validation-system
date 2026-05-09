import random

def generate_sensor_data():

    sensor_data = {
        "temp": round(random.uniform(70, 110), 2),
        "pressure": round(random.uniform(25, 35), 2),
        "vibration": round(random.uniform(2, 8), 2)
    }

    return sensor_data