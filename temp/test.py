import RPi.GPIO as GPIO
from Controller import Controller
from Motor import Motor
import time
from numpy import pi, sin, cos, sqrt, arccos, arcsin

#Test program for stepper motor

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

motor=Motor(8,10,12,16)

try:
    while True:
        direction = int(input("Input Direction: "))
        steps = int(input("Input Step Number: "))
        laservar = int(input("Laser state: "))
        GPIO.output(3,laservar)
        motor.move(direction,steps,0.01)

except KeyboardInterrupt:
    GPIO.cleanup()