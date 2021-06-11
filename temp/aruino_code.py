#include <Stepper.h>
#include <Servo.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
import time

stepsPerRevolution = 20
servoPin = 6

# Hardware Initialization
Servo penServo; #initiates servo
Stepper xAxis(stepsPerRevolution, 2, 3, 10, 11); #pins x axis motor are connected to
Stepper yAxis(stepsPerRevolution, 4, 5, 8, 9); #pins y axis motor are connected to

# Dynamic Memory Initialization
drawing,xStep,yStep,xOld,yOld,coordX,coordY = (True,None,None,None,None,None,None)


def setup():
    xAxis.setSpeed(100)
    yAxis.setSpeed(100)
    penServo.attach(servoPin)
    Serial.begin(9600)


def loop():
  while drawing == True:
    time.sleep(6000)
    numCoords = blockingRead() #reads total number of coordinates
  
    movePenUp() #initializes pen as up
    xOld = 0 #initializes, axis start at (0.0)
    yOld = 0

    for i in range(0,numCoords):
        print("@GetNext")
        time.sleep(3000)

        #python sends in next two coords
        coordX = blockingRead()
        coordY = blockingRead()

        # calculate difference
        xStep = coordX - xOld
        yStep = coordY - yOld

        if fabs(xStep) > 5 or fabs(yStep) > 5:
            movePenUp()
            drawX(int(xStep))
            drawY(int(yStep))
            movePenDown()
        else:
            drawX(int(xStep))
            drawY(int(yStep))

        xOld = coordX
        yOld = coordY
    movePenUp()
  drawing = False


def movePenUp():
  penServo.write(70)
  delay(1000)

def movePenDown():
  penServo.write(0)
  delay(1000)

def drawX(stepsToMove):
    steps = None
    if stepsToMove > 0:
        steps = 1
    else:
        stepsToMove *= -1
        steps = -1

    for i in range(0, stepsToMove):
        xAxis.step(steps)
        delay(10)

def drawY(stepsToMove):
    steps = None
    if stepsToMove > 0:
        steps = 1
    else:
        stepsToMove *= -1
        steps = -1

    for i in range(0,int(stepsToMove)):
        yAxis.step(steps)
        time.sleep(10)

def blockingRead():
    while not Serial.available():
        time.sleep(100)
    return convertSerialInputStringToInt();

def convertSerialInputStringToInt():
    resultStr,resultInt,inputString = (None,0,"")
    tempChar = Serial.read();

    #   reads entire input char by char into a string
    while tempChar != ' ' and tempChar != '\n':
        inputString += str(tempChar)
        tempChar = Serial.read()
        time.sleep(100)

    #   parses that string into an int
    for i in range(0,len(inputString)):
        if inputString[i] == '.':
            break
        elif inputString[i] >= 48 and inputString[i] <= 57:
            resultStr += inputString[i]
  
    resultInt = int(resultStr)

    return resultInt