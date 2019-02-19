import RPi.GPIO as GPIO
import dht11
import time
import datetime
import json
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=4)

#while True:
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

        
	info1 = json.dumps(log_temp)
	info2 = json.dumps(log_humi)
	loaded_temp = json.loads(info1)
	loaded_humi = json.loads(info2)

	print loaded_temp
	print "--------------"
	print loaded_humi

	url="http://192.168.0.106/logs"

	r1 = requests.post(url, json=info1)
	r2 = requests.post(url, json=info2)

	if r1.status_code != 200:
  		print "Error:", r1.status_code

	if r2.status_code != 200:
  		print "Error:", r2.status_code


	data1 = r1.json()
	print data1

	data2 = r2.json()
	print data2
#	time.sleep(10)
