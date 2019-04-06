import sqlite3
import time;
connection = sqlite3.connect("locallogs")
cursor = connection.cursor()

def createTable():
    cursor.execute("CREATE TABLE logs (timestamp TEXT, deviceId TEXT, logValue TEXT, deviceType TEXT, valuePrefix TEXT, departmentId TEXT, createdBy TEXT)")
    connection.commit()
    return True

def checkTableExist():
    cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = ? AND name = ?", ("table", "logs"))
    if (!cursor.moveToFirst()):
        return False
    return True

def insertDataIntoDatabase(data):
    cursor.execute("INSERT INTO logs (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (time.time() ,data["deviceId"], data["logValue"], data["deviceType"], data["valuePrefix"], data["departmentId"], data["createdBy"]))
    connection.commit()
    return True

def checkDataExistInDatabase(data):
    cursor.execute("SELECT * FROM logs")
    for row in cursor:
        print row
