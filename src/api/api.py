import requests
import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/constants.py')))

import constants as constant

logURL = constant.baseurl + "/logs"
sensorURL = constant.baseurl + "/sensors"

def postDataToServer(data):
    request = requests.post(logURL, data=data)
    if request.status_code != 200:
        print "Error:", request.status_code
    return

def readDataFromServer():
    request = requests.get(sensorURL)
    if request.status_code != 200:
        print "Error:", request.status_code
        return request
    else:
        return request.json()
