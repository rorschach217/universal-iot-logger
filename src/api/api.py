import requests
sys.path.append(os.path.dirname(os.path.realpath('src/constants.py')))

import sys, os

url = baseurl + "/logs"

def postDataToServer(data):
    print url
    print data
    request = requests.post(url, data=data)
    if request.status_code != 200:
            print "Error:", r1.status_code
    return
