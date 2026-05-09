def ecu(temp, pressure, vibration):

    if temp > 95:
        return "OVERHEAT WARNING"

    if pressure < 28:
        return "LOW PRESSURE ALERT"

    if vibration > 6:
        return "MECHANICAL FAULT"

    return "NORMAL"