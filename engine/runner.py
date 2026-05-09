import time

from sensors.sensors import generate_sensor_data
from ecu.controller import ecu
from validation.validator import validate
from logs.logger import append_log

def run_live_system():

    while True:

        # STEP 1 → generate live sensor values
        sensor_data = generate_sensor_data()

        # STEP 2 → ECU processes sensor values
        ecu_result = ecu(
            sensor_data["temp"],
            sensor_data["pressure"],
            sensor_data["vibration"]
        )

        # STEP 3 → validate result
        status = validate(ecu_result)

        # STEP 4 → create full payload
        payload = {
            "sensor_data": sensor_data,
            "ecu_result": ecu_result,
            "status": status,
            "timestamp": time.strftime("%H:%M:%S")
        }

        # STEP 5 → save to logs
        append_log(payload)

        # STEP 6 → print live system data
        print(payload)

        # STEP 7 → simulate real-time cycle
        time.sleep(1)