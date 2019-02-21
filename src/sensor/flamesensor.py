import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

GPIO.setup(22, GPIO.IN)
f=GPIO.input(22)

def readSensorData(parameter):
    log_flame=dict()
    result3 = GPIO.input(22)
    if result.is_valid():
        	if f==False:    #When output from motion sensor is LOW
                            log_flame["deviceId"]= "FLAME"
                            log_flame["logValue"]= result3
                            log_flame["deviceType"]= "flame"
                            log_flame["valuePrefix"]= "FLAME NOT DETECTED"
                            log_flame["departmentId"]= "PLANT"
                            log_flame["createdBy"]= "b8:27:eb:4a:65:3c"
                    else:                #When output from motion sensor is HIGH
                            log_flame["deviceId"]= "FLAME"
                            log_flame["logValue"]= result3
                            log_flame["deviceType"]= "flame"
                            log_flame["valuePrefix"]= "FLAME DETECTED"
                            log_flame["departmentId"]= "PLANT"
                            log_flame["createdBy"]= "b8:27:eb:4a:65:3c"
    api.postDataToServer(log_flame)

    return
