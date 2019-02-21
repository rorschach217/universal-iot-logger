import dht11
import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

instance = dht11.DHT11(pin=4)

def readSensorData(parameter):
    log_temp=dict()
    log_humi=dict()
    result = instance.read()
    if result.is_valid():
        log_temp["deviceId"]= "TEMPSENSE"
        log_temp["logValue"]= result.temperature
        log_temp["deviceType"]= "temperature"
        log_temp["valuePrefix"]= "degree"
        log_temp["departmentId"]= "PLANT"
        log_temp["createdBy"]= "b8:27:eb:4a:65:3c"

        log_humi["deviceId"]= "HUMISENSE"
        log_humi["logValue"]= result.humidity
        log_humi["deviceType"]= "humidity"
        log_humi["valuePrefix"]= "%"
        log_humi["departmentId"]= "PLANT"
        log_humi["createdBy"]= "b8:27:eb:4a:65:3c"
    print log_temp
    print log_humi
    postDataToServer(log_temp)
    postDataToServer(log_humi)
    return
