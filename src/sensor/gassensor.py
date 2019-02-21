import sys, os
import RPi.GPIO as GPIO

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)
g=GPIO.input(27)

def readSensorData(parameter):
    log_gas=dict()
    result2 = GPIO.input(27)
    if g==False: #When output from motion sensor is LOW
        log_gas["deviceId"]= "GAS"
        log_gas["logValue"]= result2
        log_gas["deviceType"]= "gas"
        log_gas["valuePrefix"]= "NO GAS DETECTION"
        log_gas["departmentId"]= "PLANT"
        log_gas["createdBy"]= "b8:27:eb:4a:65:3c"
    else: #When output from motion sensor is HIGH
        log_gas["deviceId"]= "GAS"
        log_gas["logValue"]= result2
        log_gas["deviceType"]= "gas"
        log_gas["valuePrefix"]= "GAS DETECTED"
        log_gas["departmentId"]= "PLANT"
        log_gas["createdBy"]= "b8:27:eb:4a:65:3c"
    api.postDataToServer(log_gas)

    return
