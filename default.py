import RPi.GPIO as GPIO
import time
import sys, os
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/dht11sensor.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/flamesensor.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/gassensor.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/irsensor.py')))

import dht11sensor as dht11sensor
import flamesensor as flamesensor
import gassensor as gassensor
import irsensor as irsensor

# initialize GPIO
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# GPIO.setup(17, GPIO.IN)
# GPIO.setup(27, GPIO.IN)
# GPIO.setup(22, GPIO.IN)

while True:
    flamesensor.readSensorData(None)
    gassensor.readSensorData(None)
    irsensor.readSensorData(None)
    dht11sensor.readSensorData(None)
    time.sleep(1)
