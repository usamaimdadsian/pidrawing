import time
import numpy as np
import RPi.GPIO as GPIO
from Motor import Motor

def GCD(a,b):
    while b:
       a, b = b, a%b
    return a

def LCM(a,b):
    return a*b/GCD(a,b)

def sign(a):
    if a>0:
        return 1
    elif a<0:
        return -1
    else:
        return 0

class Controller:
    def __init__(self):
        pass

    def motor_step(self,stepper1,step1,stepper2,step2,speed):
        dir1,dir2 = (step1,step2)
        step1,step2 = (np.abs(step1),np.abs(step2))
        
        if step1==0:
            total_micro_step=step2
            micro_step2=1
            micro_step1=step2+100

        elif step2==0:
            total_micro_step=step1
            micro_step1=1
            micro_step2=step1+100

        else:
            total_micro_step=LCM(step1,step2)
            micro_step1=total_micro_step/step1
            micro_step2=total_micro_step/step2

        T=np.sqrt(step1**2+step2**2)/speed
        dt=T/total_micro_step
    
        for i in range(1,total_micro_step+1):
            time_laps=0
            if ((i % micro_step1)==0):
                stepper1.move(dir1,1,dt/4.0)
                time_laps+=dt/4.0
                
            if ((i % micro_step2)==0):
                stepper2.move(dir2,1,dt/4.0)
                time_laps+=dt/4.0
            
            time.sleep(dt-time_laps)

        return 0