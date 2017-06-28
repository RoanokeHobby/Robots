## Welcome to the Roanoke Hobby Robots Blog 

**Home** | [GoPiGo](Page2.md) | [CamJam EduKit 3](Page3.md)

**June 28, 2017**

And so it begins! First batch of code uploaded this week are two different ways to 
program a semi-autonomous CamJam Robot using the ultrasonic distance sensor.

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
### This Page Uses Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. 
For more details, see the documentation for [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Contact

Have a comment or question about one of the projects published here? Contact darrell [at] roanokehobby [dot] net

Proudly hosted on **GitHub** ![octocat_small](https://user-images.githubusercontent.com/16419894/27620843-839a2fa6-5b9a-11e7-9ebc-76a8e713b7f7.png)
