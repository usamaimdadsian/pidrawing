import time
import RPi.GPIO as GPIO

phase_seq=[[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]
num_phase=len(phase_seq)

class Motor:
    phase, direction, position = (0,0,0)
    # Pin numbers
    a1,a2,b1,b2 = (0,0,0,0)

    def __init__(self,a1,a2,b1,b2):
        GPIO.setmode(GPIO.BOARD)
        
        self.a1,self.a2,self.b1,self.b2 = (a1,a2,b1,b2)
        
        GPIO.setup(self.a1,GPIO.OUT)
        GPIO.setup(self.a2,GPIO.OUT)
        GPIO.setup(self.b1,GPIO.OUT)
        GPIO.setup(self.b2,GPIO.OUT)

        print("Steppers Configured")
        self.phase,self.direction, self.position = (0,0,0)
    
    def move(self, direction, steps, delay=0.2):
        for _ in range(steps):
            next_phase=(self.phase+direction) % num_phase
            
            GPIO.output(self.a1,phase_seq[next_phase][0])
            GPIO.output(self.b2,phase_seq[next_phase][1])
            GPIO.output(self.a2,phase_seq[next_phase][2])
            GPIO.output(self.b1,phase_seq[next_phase][3])
            
            self.phase, self.direction= (next_phase, direction)
            self.position+=direction
        
            time.sleep(delay)
        
    def unhold(self):
        GPIO.output(self.a1,0)
        GPIO.output(self.a2,0)
        GPIO.output(self.b1,0)
        GPIO.output(self.b2,0)