import sqlite3
import time;
connection = sqlite3.connect("locallogs")
cursor = connection.cursor()

def createTable():
    cursor.execute("CREATE TABLE logs (timestamp TEXT, deviceId TEXT, logValue TEXT, deviceType TEXT, valuePrefix TEXT, departmentId TEXT, createdBy TEXT)")
    connection.commit()
    return True

def checkTableExist():
    tables = cursor.execute("SELECT * FROM information_schema.tables WHERE table_name = 'logs'")
    if (len(tables)):
        return False
    return True

def insertDataIntoDatabase(data):
    cursor.execute("INSERT INTO logs (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (time.time() ,data["deviceId"], data["logValue"], data["deviceType"], data["valuePrefix"], data["departmentId"], data["createdBy"]))
    connection.commit()
    return True

def checkDataExistInDatabase():
    cursor.execute("SELECT * FROM logs")
    for row in cursor:
        print row
