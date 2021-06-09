import cv2
import numpy as np
from Image import Image
from Drawing import Drawing


if __name__ == '__main__':
    img = cv2.imread('../img.jpeg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image(img)
    
    # plt.imshow(img.oimg)
    # plt.show()

    # Edged Image
    # plt.imshow(img.eimg,'gray')
    # plt.show()

    scene = img.eimg
    board = np.zeros_like(scene)
    d = Drawing(scene,board)
    d.startDrawing()
    # print(board.shape)

