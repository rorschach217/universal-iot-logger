import RPi.GPIO as GPIO
import dht11
import time
import requests
import sqlite3

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# connecting with database
conn = sqlite3.connect('IOT_LOCAL_LOGS')
cur = conn.cursor()

# read data using pin 4
instance = dht11.DHT11(pin=4)

while True:
	result = instance.read()
	if result.is_valid():
    		log_temp=dict()
    		log_humi=dict()
    		log_temp["deviceId"]= "TEMPSENSE"
    		log_temp["logValue"]= result.temperature
    		log_temp["deviceType"]= "temperature"
    		log_temp["valuePrefix"]= "degree"
    		log_temp["departmentId"]= "PLANT"
    		log_temp["createdBy"]= "b8:27:eb:4a:65:3c"

		log_humi["deviceId"]= "HUMISENSE"
    		log_humi["logValue"]= result.humidity
    		log_humi["deviceType"]= "humidity"
    		log_humi["valuePrefix"]= "%"
    		log_humi["departmentId"]= "PLANT"
    		log_humi["createdBy"]= "b8:27:eb:4a:65:3c"

		url="http://iotserver.codeofgyan.com/logs"
	        #url="http://192.168.137.166:8080/logs"

		r1 = requests.post(url, data=log_temp)
    		r2 = requests.post(url, data=log_humi)

		if r1.status_code != 200:
	       		print "Error:", r1.status_code

		if r2.status_code != 200:
        		print "Error:", r2.status_code

		#data1 = r1.json()
   		#print data1

		#data2 = r2.json()
    		#print data2

		ts = time.time()
		#insert temperature data into sql
		cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"TEMPSENSE", result.temperature, "temperature", "degree", "PLANT", "b8:27:eb:4a:65:3c"))

		#insert humidity data into sql
		cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"HUMISENSE", result.humidity, "humidity", "%", "PLANT", "b8:27:eb:4a:65:3c"))

		conn.commit()

		time.sleep(5)

conn.close()
