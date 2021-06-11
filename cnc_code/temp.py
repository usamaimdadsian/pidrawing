import time
from Motor import Motor

if __name__ == '__main__':
    # m1 = Motor(17,27) #11,13 
    m2 = Motor(22,23) #15,16



    while True:
        inp = input(":")
        if inp == "q":
            break
        inp = int(inp)
        dire = (inp > 0)
        # m1.move(dire,abs(inp))
        m2.move(dire,abs(inp))

