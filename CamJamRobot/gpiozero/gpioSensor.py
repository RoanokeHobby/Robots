# gpioSensor.py
# Prototype algorithm for accessing the Distance Sensor using GPIO Zero
# Date: 3/23/2017
# Author: Darrell Little - Roanoke Hobby
# GNU General Public License v3.0 (GPL-3.0)

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17, threshold_distance=0.15, max_distance=1)

def getDistance():
	d = round((sensor.distance * 100),1)
	return d

minDistance = 15

try:
	while True:
		distance = getDistance()
		if distance > minDistance:
        		print('Distance to nearest object is', distance, 'cm. Forward!')
		else:
			print('Object detected at', distance, 'cm. Reverse!')
		sleep(2)

except KeyboardInterrupt:
	print('\n')
	print('Stopping program')
