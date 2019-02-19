import RPi.GPIO as GPIO
import dht11
import time
import requests
import sqlite3

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(27, GPIO.IN)
#GPIO.setup(22, GPIO.IN)

# connecting with database
conn = sqlite3.connect('IOT_LOCAL_LOGS')
cur = conn.cursor()	# Pointer Creation

# read data using pin 4
instance = dht11.DHT11(pin=4)
i=GPIO.input(17)
#g=GPIO.input(27)
#f=GPIO.input(22)

while True:
        result = instance.read()
	result1 = GPIO.input(17)
	#result2 = GPIO.input(27)
	#result3 = GPIO.input(22)

	if result.is_valid():
                log_temp=dict()
                log_humi=dict()
		log_ir=dict()
		#log_gas=dict()
		#log_flame=disct()

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
		
		if i==False:	#When output from motion sensor is LOW
			log_ir["deviceId"]= "IR"
                	log_ir["logValue"]= result1
                	log_ir["deviceType"]= "ir"
                	log_ir["valuePrefix"]= "NO INTRUDER DETECTION"
                	log_ir["departmentId"]= "PLANT"
                	log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
		else:                #When output from motion sensor is HIGH
			log_ir["deviceId"]= "IR"
                	log_ir["logValue"]= result1
                	log_ir["deviceType"]= "ir"
                	log_ir["valuePrefix"]= "INTRUDER DETECTION"
                	log_ir["departmentId"]= "PLANT"
                	log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
		
		#if g==False:    #When output from motion sensor is LOW
                #        log_ir["deviceId"]= "GAS"
                #        log_ir["logValue"]= result2
                #        log_ir["deviceType"]= "gas"
                #        log_ir["valuePrefix"]= "NO GAS DETECTION"
                #       log_ir["departmentId"]= "PLANT"
                #        log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
                #else:                #When output from motion sensor is HIGH
                #        log_ir["deviceId"]= "GAS"
                #        log_ir["logValue"]= result2
                #        log_ir["deviceType"]= "gas"
                #        log_ir["valuePrefix"]= "GAS DETECTED"
                #        log_ir["departmentId"]= "PLANT"
                #        log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
		
		#if f==False:    #When output from motion sensor is LOW
                #        log_ir["deviceId"]= "FLAME"
                #        log_ir["logValue"]= result3
                #        log_ir["deviceType"]= "dlame"
                #        log_ir["valuePrefix"]= "FLAME NOT DETECTED"
                #       log_ir["departmentId"]= "PLANT"
                #        log_ir["createdBy"]= "b8:27:eb:4a:65:3c"
                #else:                #When output from motion sensor is HIGH
                #        log_ir["deviceId"]= "FLAME"
                #        log_ir["logValue"]= result3
                #        log_ir["deviceType"]= "flame"
                #        log_ir["valuePrefix"]= "FLAME DETECTED"
                #        log_ir["departmentId"]= "PLANT"
                #        log_ir["createdBy"]= "b8:27:eb:4a:65:3c"

               	# url="http://iotserver.codeofgyan.com/logs"
		url="http://192.168.137.166:8080/logs"

                r1 = requests.post(url, data=log_temp)
                r2 = requests.post(url, data=log_humi)
		r3 = requests.post(url, data=log_ir)
		#r4 = requests.post(url, data=log_gas)
		#r5 = requests.post(url, data=log_flame)

                if r1.status_code != 200:
                        print "Error:", r1.status_code

                if r2.status_code != 200:
                        print "Error:", r2.status_code

		if r3.status_code != 200:
                        print "Error:", r3.status_code
		
		#if r3.status_code != 200:
                #        print "Error:", r3.status_code
		
		#if r3.status_code != 200:
                #        print "Error:", r3.status_code

		ts = time.time()
                
		#insert temperature data into sql
                cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"TEMPSENSE", result.temperature, "temperature", "degree", "PLANT", "b8:27:eb:4a:65:3c"))

                #insert humidity data into sql
                cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"HUMISENSE", result.humidity, "humidity", "%", "PLANT", "b8:27:eb:4a:65:3c"))

		#insert nir data into sql
                cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"IR", result1, "ir", "NO INTRUDER DETECTION", "PLANT", "b8:27:eb:4a:65:3c"))
        
		#insert ir data into sql
                cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"IR", result1, "ir", "INTRUDER DETECTION", "PLANT", "b8:27:eb:4a:65:3c"))

		#insert ng data into sql
		#cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"GAS", result2, "gas", "GAS NOT DETECTED", "PLANT", "b8:27:eb:4a:65:3c"))

		#insert g data into sql
		#cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"GAS", result2, "gas", "GAS DETECTED", "PLANT", "b8:27:eb:4a:65:3c"))

		#insert nf data into sql
		#cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"FLAME", result3, "flame", "FLAME NOT DETECTED", "PLANT", "b8:27:eb:4a:65:3c"))

		#insert ng data into sql
		#cur.execute("INSERT INTO LOCAL_LOGS (timestamp, deviceId, logValue, deviceType, valuePrefix, departmentId, createdBy) VALUES (?, ?, ?, ?, ?, ?, ?)", (ts,"GAS", result3, "gas", "FLAME NOT DETECTED", "PLANT", "b8:27:eb:4a:65:3c"))
	        
		conn.commit()

                time.sleep(10)

conn.close()
