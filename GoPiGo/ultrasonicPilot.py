#!/usr/bin/env python

#################################################################################
#  ultrasonicPilot.py								#
#  Darrell Little								#
#  07/01/2017									#
#  Obstacle avoidance with a fixed ultrasonic sensor				#
#  Based on "Programming Autonomy - 						#
#  Robotics with Python Raspberry Pi and GoPiGo p.6"				#
#  https://pythonprogramming.net/programming-autonomous-robot-gopigo-tutorial/	#
#################################################################################

from gopigo import *
import time
import random

min_distance = 25
fwdSpeed = 150
revSpeed = 175

# Blink both LED
def blink():
    for x in range(0, 4):
	led_on(0)
        led_on(1)
        time.sleep(0.5)
        led_off(0)
        led_off(1)

def autoPilot():
    # Continuously loop unless REVERSE repeats too many times
    max_reverse = 2
    reverse_attempt = 0
    no_problem = True
    # When REVERSE needed, choose random rotate right or rotate left
    rot_choices = [right_rot, left_rot]
    
    while no_problem:
        time.sleep(0.25)
        dist = us_dist(15)
        if dist > min_distance:
            print('Forward is clear', dist)
	    # Reset reverse_attempt if able to move forward
	    reverse_attempt = 0
            set_speed(fwdSpeed)
            fwd()
            time.sleep(0.25)
        else:
            print('Obstacle detected', dist)
            stop()
	    if reverse_attempt < max_reverse:
	        print('REVERSE!')
	        blink()
                set_speed(revSpeed)
                bwd()
                time.sleep(0.5)
                rotation = rot_choices[random.randrange(0,2)]
                rotation()
                # Increment for each attempt at REVERSE
                reverse_attempt +=1
	        time.sleep(0.25)
	    else:
	        stop()
	        print('Houston, we have a problem!')
	        print('Stopping Program')
	        no_problem = False
    stop()

stop()
print('Wait for sensor to stabilize')
time.sleep(1)
print('One ... ', us_dist(15))
time.sleep(1)
print('Two ... ', us_dist(15))
time.sleep(1)
print('Three ... ', us_dist(15))
time.sleep(1)
print('GoPiGo!')

try:
    autoPilot()

except KeyboardInterrupt:
    stop()
    print('Stopping Program')
