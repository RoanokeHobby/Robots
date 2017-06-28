### Welcome to Page Three

[Home](README.md) | [GoPiGo](Page2.md) | **CamJam EduKit 3**

**June 28, 2017**

Started with the CamJam code for using the distance sensor.
Next, I took a dive into using GPIO Zero to accomplish the same goal.

Experimenting with the sensor, right away you'll see there is a lot of stuff built in:
```python
from gpiozero import DistanceSensor
from time import sleep
```
Then instantiate your DistanceSensor object and begin taking measurements:
```python
sensor = DistanceSensor(echo=18, trigger=17, threshold_distance=0.15, max_distance=1)

def getDistance():
        d = round((sensor.distance * 100),1)
        return d

minDistance = 15
```
Put it all together inside of a Try statement:
```python
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
```
Tada! You're well on your way to avoiding objects using the ultrasonic sensor! 
Next time I'll go into a little more detail putting this together with controlling the motors.

* * *
Yippie! This page will contain posts related to the [CamJam EduKit 3](https://camjam.me/?page_id=1035).

Unless otherwise noted, code for the **CamJam EduKit 3** will be in Python 3. Opinions expressed here are my own and not associated with [Cambridge Raspberry Jam](http://camjam.me/) or [The Pi Hut](https://thepihut.com/). Occasionally, I'll be experimenting with [GPIO Zero](https://gpiozero.readthedocs.io/), created by [Ben Nuttall](https://github.com/bennuttall) of the [Raspberry Pi Foundation](https://www.raspberrypi.org/), [Dave Jones](https://github.com/waveform80) and other contributors. Many thanks to all of the above for their many contributions to the DIY maker community!

>Have you noticed the amazing coincidences occuring on this site yet? Page three - Python 3 - EduKit 3. Mind boggling, isn't it?
