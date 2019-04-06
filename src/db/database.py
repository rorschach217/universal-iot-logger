import sqlite3, time, sys, os

sys.path.append(os.path.dirname(os.path.realpath('src/api/api.py')))

import api as api

connection = sqlite3.connect("locallogs")
cursor = connection.cursor()

def createTable():
    cursor.execute("CREATE TABLE if not exists logs (timestamp TEXT, deviceId TEXT, logValue TEXT, deviceType TEXT, valuePrefix TEXT, departmentId TEXT, createdBy TEXT)")
    connection.commit()
    return True

def insertDataIntoDatabase(data):
    cursor.execute("INSERT INTO logs (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (time.time() ,data["deviceId"], data["logValue"], data["deviceType"], data["valuePrefix"], data["departmentId"], data["createdBy"]))
    connection.commit()
    return True

def checkDataExistInDatabase():
    cursor.execute("SELECT * FROM logs")
    for row in cursor:
        data = dict()
        data["timestamp"]= row[0]
        data["deviceId"]= row[1]
        data["logValue"]= row[2]
        data["deviceType"]= row[3]
        data["valuePrefix"]= row[4]
        data["departmentId"]= row[5]
        data["createdBy"]= row[6]
        check = api.postLocalDataToServer(data)
        if check:
            cursor.execute("DELETE FROM logs WHERE timestamp = " + row[0])
            connection.commit()
