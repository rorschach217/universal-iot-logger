import sys, os
import RPi.GPIO as GPIO

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
result=GPIO.input(17)

def readSensorData(parameter):
    log_ir=dict()
    if result.is_valid():
    	if i==False: #When output from motion sensor is LOW
		log_ir["deviceId"]= "IR"
    	log_ir["logValue"]= result
    	log_ir["deviceType"]= "ir"
    	log_ir["valuePrefix"]= "NO INTRUDER DETECTION"
    	log_ir["departmentId"]= "PLANT"
    	log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
	else: #When output from motion sensor is HIGH
		log_ir["deviceId"]= "IR"
    	log_ir["logValue"]= result
    	log_ir["deviceType"]= "ir"
    	log_ir["valuePrefix"]= "INTRUDER DETECTION"
    	log_ir["departmentId"]= "PLANT"
    	log_ir["createdBy"]= "b8:27:eb:4a:65:3c"

    api.postDataToServer(log_ir)

    return
