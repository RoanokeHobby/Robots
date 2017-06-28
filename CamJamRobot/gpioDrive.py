from gpiozero import CamJamKitRobot, DistanceSensor
from time import sleep

myBot = CamJamKitRobot()
sensor = DistanceSensor (echo=18, trigger=17, threshold_distance=0.15, max_distance=1)

def driveForward():
	if sensor.distance > 0.15:
		print('Clear Distance: ', sensor.distance * 100, 'cm')
		myBot.forward(0.5)
	else:
		print('Halt Program, objects too close!')
		myBot.stop()

def avoidObstacle():
	myBot.stop()
	sleep(1)
	print('Obstacle Detected at ', sensor.distance * 100, 'cm. Change Course')
	sleep(1)
	myBot.backward()
	sensor.wait_for_out_of_range()
	myBot.stop()
	sleep(1)
	myBot.left(0.5)
	sleep(0.5)
	myBot.stop()
	sleep(1)

try:
	while True:
		if sensor.distance > 0.15:
			driveForward()
			sensor.wait_for_in_range()
			avoidObstacle()
		else:
			print('Halt Program, objects are too close!')
			myBot.stop()
			break

except KeyboardInterrupt:
	print('\n')
	print('Stopping Program')
	myBot.stop()
	myBot.close()

