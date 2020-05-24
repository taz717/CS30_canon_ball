'''
Moataz Khallaf
Cannon BOI
Oct 12, 2018
'''
import time
import math
from Subroutines import * ##Big library hours

###Inputs
x = menu()
gravity = 9.81 ##Just cuz also this is acceleration.
##scene 1
if x == "1":
    speed = askSpeed()
    height = askHeight()
##scene 2
elif x == "2":
    speed = askSpeed()  ##what is this a survey?
    angle = askAngle()
##scene 3
elif x == "3":
    speed = askSpeed()
    height = askHeight()
    angle = askAngle()

##Scene 4
# The idea behind scene 4 is that I need marks... and all I remember from last year is that
# the speed that the ball is right after it's fired is the same as the speed right before it's about to land.
# Also that it's speed is 0 when it reaches peak height but that doesn't matter

else:
    speed = askSpeed()
    print("did you know that the speed of the ball right after it's fired from the cannon is the same as when it's right about to land??? ")
                                                                                                                                                                                                                                                                                                                                                                        
###Proccessing
##scene 1
if x == "1":
    otherTime = sceneOneTime(height)
    distance = sceneOneDistance(otherTime, speed)
##scene 2
elif x == "2":
    rad = convertRad(angle)
    speedH = findSpeedH(speed, rad)
    speedV = findSpeedV(speed, rad)
    otherTime = sceneTwoTime(speedV)
    distance = (otherTime * 2) * speedH ##too lazy to turn into fuction to be honest.
##scene 3
elif x == "3":
    rad = convertRad(angle)
    speedV = findSpeedV(speed, rad)
    speedFSqaured = math.pow(speedV, 2) + (2 * gravity * height)
    speedF = math.sqrt(speedFSqaured)
    otherTime = sceneThreeTime(speedF, speedV) ##just to stay consistant. I've realized how useless these commands are but whatever
    speedH = findSpeedH(speed, rad)
    distance  = speedH * otherTime

else:
    distance = (speed** 2) / (2* gravity)

###Outputs
##all scenes cuz of this godly function BLESS ALL HAIL THE RESULT FUNCTION
result(distance) ##YEET WE ARE DONE FELLAS AND LADY FELLAS, hopefully this is better than the last