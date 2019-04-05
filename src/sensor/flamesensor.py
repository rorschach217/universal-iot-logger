import sys, os
# import RPi.GPIO as GPIO

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

# GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)
result=GPIO.input(22)

def readSensorData(parameter):
    log_flame=dict()
    print(result)
    if GPIO.input(22).is_valid():
    	if result==False: #When output from motion sensor is LOW
	        log_flame["deviceId"]= "FLAME"
        	log_flame["logValue"]= result
        	log_flame["deviceType"]= "flame"
        	log_flame["valuePrefix"]= "FLAME NOT DETECTED"
        	log_flame["departmentId"]= "PLANT"
        	log_flame["createdBy"]= "b8:27:eb:4a:65:3c"
        else: #When output from motion sensor is HIGH
        	log_flame["deviceId"]= "FLAME"
        	log_flame["logValue"]= result
        	log_flame["deviceType"]= "flame"
        	log_flame["valuePrefix"]= "FLAME DETECTED"
        	log_flame["departmentId"]= "PLANT"
        	log_flame["createdBy"]= "b8:27:eb:4a:65:3c"

    api.postDataToServer(log_flame)

    return
