import time
from Motor import Motor

if __name__ == '__main__':
    m1 = Motor(17,27) #11,13 
    m2 = Motor(22,23) #15,16


    while True:
        m1.move(clockwise=False,steps=200)
        m2.move(True,200)
