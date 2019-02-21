import sys, os
import RPi.GPIO as GPIO

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

GPIO.setup(17, GPIO.IN)
i=GPIO.input(17)

def readSensorData(parameter):
    log_ir=dict()
    result1 = GPIO.input(17)
    if result.is_valid():
    	if i==False: #When output from motion sensor is LOW
			log_ir["deviceId"]= "IR"
        	log_ir["logValue"]= result1
        	log_ir["deviceType"]= "ir"
        	log_ir["valuePrefix"]= "NO INTRUDER DETECTION"
        	log_ir["departmentId"]= "PLANT"
        	log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
		else: #When output from motion sensor is HIGH
			log_ir["deviceId"]= "IR"
        	log_ir["logValue"]= result1
        	log_ir["deviceType"]= "ir"
        	log_ir["valuePrefix"]= "INTRUDER DETECTION"
        	log_ir["departmentId"]= "PLANT"
        	log_ir["createdBy"]= "b8:27:eb:4a:65:3c"

    api.postDataToServer(log_ir)

    return
