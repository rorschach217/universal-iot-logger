import sys, os, time

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

def readSensorData(result):
    log_ultrasonic=dict()
    if result==False:
        log_ultrasonic["deviceId"]= "ULTRASONIC"
        log_ultrasonic["logValue"]= 1
        log_ultrasonic["deviceType"]= "ultrasonic"
        log_ultrasonic["valuePrefix"]= "MOTION DETECTED"
        log_ultrasonic["departmentId"]= "PLANT"
        log_ultrasonic["createdBy"]= "b8:27:eb:4a:65:3c"
    else:
        log_ultrasonic["deviceId"]= "ULTRASONIC"
        log_ultrasonic["logValue"]= 0
        log_ultrasonic["deviceType"]= "ultrasonic"
        log_ultrasonic["valuePrefix"]= "NO MOTION DETECTED"
        log_ultrasonic["departmentId"]= "PLANT"
        log_ultrasonic["createdBy"]= "b8:27:eb:4a:65:3c"
    # api.postDataToServer(log_ultrasonic)
    print(log_ultrasonic);
    return

def distance(GPIO):
    GPIO.output(18, True)

    time.sleep(0.00001)
    GPIO.output(18, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(24) == 0:
        StartTime = time.time()

    while GPIO.input(24) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance
