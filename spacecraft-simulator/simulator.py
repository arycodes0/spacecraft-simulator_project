"""Display simulated battery and temperature readings with any alerts."""

from battery import check_battery
from temperature import check_temperature


if __name__ == "__main__":
    # Example readings for testing the simulator.
    battery = 30
    temperature = 55

    print(f"Battery: {battery}%", check_battery(battery))
    print(f"Temperature: {temperature}°C", check_temperature(temperature))