import RPi.GPIO as GPIO
import time
import sys, os
sys.path.append(os.path.dirname(os.path.realpath('src/sensor/dht11sensor.py')))

import dht11sensor as dht11sensor

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:    
    dht11sensor.readSensorData(None)
    time.sleep(10)
