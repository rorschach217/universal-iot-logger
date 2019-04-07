import sys, os, time

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

def readSensorData(result):
    log_ultrasonic=dict()
    log_ultrasonic["deviceId"]= "ULTRASONIC"
    log_ultrasonic["logValue"]= result
    log_ultrasonic["deviceType"]= "ultrasonic"
    log_ultrasonic["valuePrefix"]= "CENTEMETER"
    log_ultrasonic["departmentId"]= "PLANT"
    log_ultrasonic["createdBy"]= "b8:27:eb:4a:65:3c"
    api.postDataToServer(log_ultrasonic)
    return

def distance(GPIO, sensor):
    GPIO.setup(sensor["pin"], GPIO.OUT)
    GPIO.setup(24, GPIO.IN)

    GPIO.output(sensor["pin"], True)

    time.sleep(0.00001)
    GPIO.output(sensor["pin"], False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(24) == 0:
        StartTime = time.time()

    while GPIO.input(24) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance
