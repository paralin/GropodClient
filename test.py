import requests
import sensor

ec = sensor.readEC()
print("EC = ", ec)

ph = sensor.readPH()
print("PH = ", ph)


url = 'http://35.184.156.248:5000/sensor'
data = {'ec':ec, 'ph':ph}
headers = {'Content-Type' : 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)
