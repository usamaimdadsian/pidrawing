import numpy as np
from Motor import Motor

# TODO check how many rotations it takes to cover the whole board
class Controller:
    def __init__(self,scene,board):
        self.mx,self.my = (Motor(11,13),Motor(15,16))
        self.initPos()
        self.z = False

    def moveAt(self,x,y,draw=False,adjacent=False,left=True):
        # TODO write code to move at x,y
        if draw: self.pencil(True)
        if not adjacent: self.pencil(False)
            
    def pencil(self,draw):
        if draw:
            # TODO Write code to move servo for drawing 
            self.z = True
        else:
            # TODO code to move pencil to initial position
            self.z = False
    
    def initPos(self):
        self.pencil(False)
        # TODO try to move motors mx and my to left and bottom as much as possible
        self.x,self.y = (0,0)
        


# motors can be move in steps