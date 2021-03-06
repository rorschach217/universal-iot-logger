import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

def readSensorData(result):
    log_pir=dict()
    if result==False:
        log_pir["deviceId"]= "PIR"
        log_pir["logValue"]= 1
        log_pir["deviceType"]= "pir"
        log_pir["valuePrefix"]= "MOTION DETECTED"
        log_pir["departmentId"]= "PLANT"
        log_pir["createdBy"]= "b8:27:eb:4a:65:3c"
    else:
        log_pir["deviceId"]= "PIR"
        log_pir["logValue"]= 0
        log_pir["deviceType"]= "pir"
        log_pir["valuePrefix"]= "NO MOTION DETECTED"
        log_pir["departmentId"]= "PLANT"
        log_pir["createdBy"]= "b8:27:eb:4a:65:3c"
    # api.postDataToServer(log_pir)
    print(log_pir);
    return


# GPIO.setup(18, GPIO.IN)
# GPIO.setup(23, GPIO.OUT)
# print GPIO.input(18)
# if GPIO.input(18):
#     GPIO.output(23, True)
#     time.sleep(1)
#     GPIO.output(23, False)
# pirsensor.readSensorData(GPIO.input(18))
