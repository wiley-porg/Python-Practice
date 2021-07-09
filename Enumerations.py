# "enumerate" common data (days of the week, sensor data, etc)

from enum import Enum

class Sensor(Enum):
    Temperature = 100       #must be unique - can't override to use enum


print(Sensor.Temperature)           # Sensor.Temperature

# Enums add more methods. Now, you can access both the NAME and VALUE of an object
# defined off an enumeration


print(Sensor.Temperature.name)      # Temperature
print(Sensor.Temperature.value)     # 100














