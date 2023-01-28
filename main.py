from sensors import Sensors
from humidifier import Humidifier
from fan import Fan

sensors = Sensors()
fan = Fan(sensors)
humidifier = Humidifier(sensors)

sensors.read_data(29, 62)
sensors.read_data(20, 29)
sensors.read_data(23, 60)
