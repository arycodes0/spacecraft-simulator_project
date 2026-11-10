MAX_TEMPERATURE_C = 50


def check_temperature(temperature_c: float) -> str:
    if temperature_c > MAX_TEMPERATURE_C:
        return "HIGH TEMPERATURE"
    return ""