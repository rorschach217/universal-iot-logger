import RPi.GPIO as GPIO
import dht11
import time
import sys, os
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

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dht11 = dht11.DHT11(pin=4)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)

while True:
    sensors = api.readDataFromServer()
    for sensor in sensors:
        print sensor
    # flamesensor.readSensorData(GPIO.input(22))
    # gassensor.readSensorData(GPIO.input(27))
    # irsensor.readSensorData(GPIO.input(17))
    # dht11sensor.readSensorData(dht11.read())
    time.sleep(5)
