import cv2
import numpy as np
from Image import Image
from Drawing import Drawing
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO




if __name__ == '__main__':
    inPin = 24
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(inPin,GPIO.IN)
    while True:
        value = GPIO.input(inPin)
        if value:
            print("Button pressed")
    # img = cv2.imread('index.jpeg')
    # img_o = Image(img,'edge')
    # img = img_o.rimg

    # img = cv2.imread('test.png',0)
    # img[img > 127] = 150
    # img[img < 127] = 1
    # img[img == 150] = 0

    # scene = img
    # board = np.zeros_like(scene)
    # d = Drawing(scene,board)
    # d.startDrawing()
    GPIO.cleanup()