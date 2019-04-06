import requests
import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/constants.py')))
sys.path.append(os.path.dirname(os.path.realpath('src/db/database.py')))

import constants as constant
import database as database

logURL = constant.baseurl + "/logs"
errorLogURL = constant.baseurl + "/error/logs"
sensorURL = constant.baseurl + "/sensors"

def postDataToServer(data):
    request = requests.post(logURL, data=data)
    if request.status_code != 200:
        print "Error:", request.status_code
        database.insertDataIntoDatabase(data)
    else:
        database.checkDataExistInDatabase()
    return

def readDataFromServer():
    request = requests.get(sensorURL)
    if request.status_code != 200:
        print "Error:", request.status_code
        return request
    else:
        return request.json()

def postErrorToServer(message, sensor, deviceId, mac):
    error=dict()
    error["deviceId"]= deviceId
    error["sensor"]= sensor
    error["message"]= message
    error["createdBy"]= mac
    request = requests.post(errorLogURL, data=error)
    if request.status_code != 200:
        print "Error:", request.status_code
    return
