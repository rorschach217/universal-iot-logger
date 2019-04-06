import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

def readSensorData(result):
    log_gas=dict()
    if result==False:
        log_gas["deviceId"]= "GAS"
        log_gas["logValue"]= 1
        log_gas["deviceType"]= "gas"
        log_gas["valuePrefix"]= "GAS DETECTION"
        log_gas["departmentId"]= "PLANT"
        log_gas["createdBy"]= "b8:27:eb:4a:65:3c"
    else:
        log_gas["deviceId"]= "GAS"
        log_gas["logValue"]= 0
        log_gas["deviceType"]= "gas"
        log_gas["valuePrefix"]= "NO GAS DETECTED"
        log_gas["departmentId"]= "PLANT"
        log_gas["createdBy"]= "b8:27:eb:4a:65:3c"
    api.postDataToServer(log_gas)
    return
