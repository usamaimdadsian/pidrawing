import numpy as np
from Motor import Motor

# TODO check how many rotations it takes to cover the whole board
class Controller:
    # XMAX = 1900
    # yMax = 1780
    def __init__(self,scene,board):
        self.mx,self.my = (Motor(11,13),Motor(15,16))
        self.initPos()
        self.z = False

    def moveAt(self,x,y,draw=False,adjacent=False,left=True):
        # TODO write code to move at x,y
        self.mx.move(x-self.x)
        self.my.move(y-self.y)

        self.x, self.y = (x,y)
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
        # TODO try to move motors mx and my to right and bottom as much as possible
        self.moveAt(0,0,draw=False)
        


# motors can be move in steps