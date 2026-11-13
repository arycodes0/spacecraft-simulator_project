MAX_TEMPERATURE_C = 50


def check_temperature(temperature_c: float) -> str:
    """Return a high-temperature alert or an empty string."""
    if temperature_c > MAX_TEMPERATURE_C:
        return "HIGH TEMPERATURE"
    return ""