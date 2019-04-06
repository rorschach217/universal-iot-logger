import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

def temperatureData(result):
    log_temp=dict()
    if result.is_valid():
        log_temp["deviceId"]= "TEMPSENSE"
        log_temp["logValue"]= result.temperature
        log_temp["deviceType"]= "temperature"
        log_temp["valuePrefix"]= "degree"
        log_temp["departmentId"]= "PLANT"
        log_temp["createdBy"]= "b8:27:eb:4a:65:3c"
    if log_temp:
        api.postDataToServer(log_temp)

def humidityData(result):
    log_humi=dict()
    if result.is_valid():
        log_humi["deviceId"]= "HUMISENSE"
        log_humi["logValue"]= result.humidity
        log_humi["deviceType"]= "humidity"
        log_humi["valuePrefix"]= "%"
        log_humi["departmentId"]= "PLANT"
        log_humi["createdBy"]= "b8:27:eb:4a:65:3c"
    if log_humi:
        api.postDataToServer(log_humi)

def readSensorData(result):
    temperatureData(result)
    humidityData(result)
    return
