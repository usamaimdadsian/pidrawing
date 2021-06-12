import time
from Motor import Motor

if __name__ == '__main__':
    m1 = Motor(17,27) #11,13 
    # m2 = Motor(22,23) #15,16



    while True:
        inp = input(":")
        if inp == "q":
            break
        m1.move(int(inp))
        # m2.move(int(inp))

