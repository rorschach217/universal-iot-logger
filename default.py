import RPi.GPIO as GPIO
import dht11
import time, sys, os, json
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/dht11sensor.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/flamesensor.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/gassensor.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/irsensor.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api
import dht11sensor as dht11sensor
import flamesensor as flamesensor
import gassensor as gassensor
import irsensor as irsensor

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
    sensors = api.readDataFromServer()
    for sensor in sensors:
        print sensor
        if sensor["sensor"] == "temperature" and sensor["isEnabled"] == True:
            dht11Object = dht11.DHT11(pin=sensor["pin"])
            dht11sensor.readTemperatureSensorData(dht11Object.read())
        if sensor["sensor"] == "humidity" and sensor["isEnabled"] == True:
            dht11Object = dht11.DHT11(pin=sensor["pin"])
            dht11sensor.readhumiditySensorData(dht11Object.read())
        if sensor["sensor"] == "infrared" and sensor["isEnabled"] == True:
            GPIO.setup(sensor["pin"], GPIO.IN)
            irsensor.readSensorData(GPIO.input(sensor["pin"]))
        if sensor["sensor"] == "gas" and sensor["isEnabled"] == True:
            GPIO.setup(sensor["pin"], GPIO.IN)
            gassensor.readSensorData(GPIO.input(sensor["pin"]))
        if sensor["sensor"] == "flame" and sensor["isEnabled"] == True:
            GPIO.setup(sensor["pin"], GPIO.IN)
            flamesensor.readSensorData(GPIO.input(sensor["pin"]))
    time.sleep(5)
