import time
import schedule
import datetime
import sensor
import requests

wiringpi.wiringPiSetup()

wiringpi.pinMode(2,1)
wiringpi.digitalWrite(2,1)

wiringpi.pinMode(0,1)
wiringpi.digitalWrite(0,1)

url = 'http://35.184.156.248:5000/sensor'

def enable():
	wiringpi.digitalWrite(2,1)

def disable():
	wiringpi.digitalWrite(2,0)

def readSensors():
	ec = sensor.readEC()
	ph = sensor.readPH()
	data = {'ec': ec, 'ph': ph}
	headers = {'Content-Type' : 'application/json'}
	r = requests.post(url, data=json.dumps(data), headers=headers)

schedule.every().day.at("17:00").do(disable)
schedule.every().day.at("01:00").do(enable)
schedule.every(5).minutes.do(readSensors)

while True:
	schedule.run_pending()
	time.sleep(1)
