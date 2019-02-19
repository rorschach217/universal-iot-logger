import imp
import time
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

dht11 = imp.load_source('dht11', 'src/sensor/dht11.py')

# initialize GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

while True:
    print dht11
    print dht11.readSensorData
    dht11.readSensorData(None)
    time.sleep(10)
