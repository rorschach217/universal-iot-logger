import requests
import imp

constants = imp.load_source('constants', '../constants.py')

url = constants.baseurl + "/logs"

def postDataToServer(data):
    request = requests.post(url, data=data)
    if request.status_code != 200:
            print "Error:", r1.status_code
    return
