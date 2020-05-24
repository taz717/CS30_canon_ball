### Subroutines for everything is name is kinda wrong :)
import math
import time
##I can name my kids easier than these variables
###Inputs

def cough(): ## this is too make sure that they only choose between 3 scenarios
    x = input("*cough* ")
    if x == "1" or x == "2" or x == "3" or x == "4":
        return x
    else:
        return cough()

def menu(): ##starting menu
    print('''
This Program caculates the distance a cannon ball travels from a few different scenarios...
Choose the following scenarios 
1. Speed of ball right after cannon fires, Height of cannon above the water

2. Speed of the cannonball immediately after it leaves the canon. 
Angle of the cannon when the cannonball leaves the canon.

3. Speed of the cannonball immediately after it leaves the canon. 
Angle of the cannon when the cannonball leaves the canon. 
Height of the canon above the enemy ship.

4. This is just the peak distance travelled when the cannon fires straight up
    ''') ##idk about #4 cheif. I wouldn't be mad if you didn't count it for marks.
    x = input("choice: ")
    if x == "1" or x == "2" or x == "3" or x == "4":
        return x
    else:
        return cough()
    
'''def scenOneInt():
    global height, speed
    print("Righty you picked height and speed soo ...")
    time.sleep(1)
    speed = float(input("speed?"))
    time.sleep(1)
    height = float(input("Height"))
    #print(height)
    return height, speed
'''

def askSpeed():
    a = float(input("speed(m/s)? "))
    return a

def askHeight():
    b = float(input("height(m)? "))
    return b

def askAngle():
    c = int(input("angle(deg)? "))
    return c

###Proccessing
gravity = 9.81
##it's kinda weird to pin point which sub is for which but for the most part this is scene 1
def sceneOneTime(a):
    x = math.sqrt(((2*a)/9.81))
    return x

def sceneOneDistance(a, b):
    x = a * b
    return x
##scene 2 and 3 subs
def convertRad(a):
    x = math.radians(a)
    return x

def findSpeedH(a, b):
    x = a * math.cos(b)
    return x

def findSpeedV(a, b):
    x = a * math.sin(b)
    return x

def sceneTwoTime(a):
    x = a / gravity
    return x

def sceneThreeTime(a,b):
    x = (a + b) / gravity
    return x 


###outputs 

def result(a):
    print("The distance in meters is:", a)