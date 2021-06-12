import cv2
import numpy as np
from Image import Image
from Drawing import Drawing
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # img = cv2.imread('img.jpeg')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img = Image(img)
    
    # plt.imshow(img)
    # plt.show()

    img = np.zeros((200,200),np.uint8)
    img[25:75,10:190] = 255
    img[100:160,10:190] = 255
    img = cv2.resize(img,(0,0), fx=178/200, fy=190/200, interpolation = cv2.INTER_AREA)
    img[img>0] = 1

    scene = img
    board = np.zeros_like(scene)
    d = Drawing(scene,board)
    d.startDrawing()

    # Edged Image
    # plt.imshow(img.eimg,'gray')
    # plt.show()

    # scene = img.eimg
    # board = np.zeros_like(scene)
    # d = Drawing(scene,board)
    # d.startDrawing()
    # print(board.shape)

