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

    #  Two Squares
    # img = np.zeros((200,200),np.uint8)
    # img[25:75,10:190] = 255
    # img[100:160,10:190] = 255
    # img = cv2.resize(img,(0,0), fx=178/200, fy=190/200, interpolation = cv2.INTER_AREA)
    # img[img>0] = 1


    # My Image
    gimg = cv2.imread("img.jpeg",0)
    igimg = 255 - gimg
    blurred_img = cv2.GaussianBlur(igimg, (21,21),0)
    inv_blurred_img = 255 - blurred_img
    pencil_sketch_img = cv2.divide(gimg,inv_blurred_img, scale = 256.0)
    pencil_sketch_img = cv2.bitwise_not(pencil_sketch_img)
    pencil_sketch_img[pencil_sketch_img>127] = 255
    img_y, img_x = pencil_sketch_img.shape[:2]
    img = cv2.resize(pencil_sketch_img,(0,0), fx=178/img_x, fy=190/img_y, interpolation = cv2.INTER_AREA)
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

