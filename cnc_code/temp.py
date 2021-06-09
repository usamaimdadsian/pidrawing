import time
from Motor import Motor

if __name__ == '__main__':
    m1 = Motor(11,13)
    m2 = Motor(15,16)
    m3 = Motor(18,22)


    while True:
        m1.move(clockwise=True,steps=200)
        m2.move(True,200)
        m3.move(True,200)
        time.sleep(1)