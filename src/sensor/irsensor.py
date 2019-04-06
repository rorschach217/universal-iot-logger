import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

def readSensorData(result):
    log_ir=dict()
    if result==False:
        log_ir["deviceId"]= "IR"
        log_ir["logValue"]= 0
        log_ir["deviceType"]= "ir"
        log_ir["valuePrefix"]= "NO INTRUDER DETECTION"
        log_ir["departmentId"]= "PLANT"
        log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
    else:
        log_ir["deviceId"]= "IR"
        log_ir["logValue"]= 1
        log_ir["deviceType"]= "ir"
        log_ir["valuePrefix"]= "INTRUDER DETECTION"
        log_ir["departmentId"]= "PLANT"
        log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
    api.postDataToServer(log_ir)
    return
