import cv2
import numpy as np
from Image import Image
from Drawing import Drawing
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # img = cv2.imread('index.jpeg')
    # img_o = Image(img,'edge')
    # img = img_o.rimg

    img = cv2.imread('test.png',0)
    img[img > 127] = 150
    img[img < 127] = 1
    img[img == 150] = 0

    scene = img
    board = np.zeros_like(scene)
    d = Drawing(scene,board)
    d.startDrawing()
