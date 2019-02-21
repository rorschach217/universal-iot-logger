import requests
import sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/constants.py')))

import constants as constant

url = constant.baseurl + "/logs"

def postDataToServer(data):
    print data
    print type(data)
    request = requests.post(url, data=data)
    if request.status_code != 200:
            print "Error:", request.status_code
    return
