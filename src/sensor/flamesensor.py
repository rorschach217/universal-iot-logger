import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

def readSensorData(result):
    log_flame=dict()
    if result==False:
        log_flame["deviceId"]= "FLAME"
        log_flame["logValue"]= 1
        log_flame["deviceType"]= "flame"
        log_flame["valuePrefix"]= "FLAME DETECTED"
        log_flame["departmentId"]= "PLANT"
        log_flame["createdBy"]= "b8:27:eb:4a:65:3c"
    else:
        log_flame["deviceId"]= "FLAME"
        log_flame["logValue"]= 0
        log_flame["deviceType"]= "flame"
        log_flame["valuePrefix"]= "FLAME NOT DETECTED"
        log_flame["departmentId"]= "PLANT"
        log_flame["createdBy"]= "b8:27:eb:4a:65:3c"
    api.postDataToServer(log_flame)
    return
