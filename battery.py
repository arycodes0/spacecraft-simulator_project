"""Battery check for the spacecraft simulator."""

LOW_BATTERY_PERCENT = 30


def check_battery(battery_percent: float) -> str:
    """Return the low-battery alert or an empty string."""
    if 0 <= battery_percent <= LOW_BATTERY_PERCENT:
        return "LOW BATTERY"
    return ""