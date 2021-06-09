import cv2

class Image:
    def __init__(self, img):
        self.prepareImage(img)

    def prepareImage(self,img):
        # Resize Image
        img_x, img_y = img.shape[:2]
        rescaleFactor = 200/img_x if (img_x > img_y) else 200/img_y
        self.oimg = cv2.resize(img, (0,0), fx=rescaleFactor, fy=rescaleFactor, interpolation = cv2.INTER_AREA) #common interpolation for shrinking
        img_y, img_x = self.oimg.shape[:2]

        # Convert to black and white
        gimg = cv2.cvtColor(self.oimg,cv2.COLOR_BGR2GRAY)
        (thresh, bwimg) = cv2.threshold(gimg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        self.bwimg = bwimg
        self.gimg = gimg
        # thresh = 127
        # bwimg= cv2.threshold(gimg, thresh, 255, cv2.THRESH_BINARY)[1]


        # Edge Detection
        imgBlurredColour = cv2.GaussianBlur(self.oimg, (7,7),0) #blurs to soften edges, really sure how effetive this is yet
        imgBlurredBlackWhite = cv2.GaussianBlur(self.bwimg, (7,7),0)

        imgOutlinedColour = cv2.Canny(imgBlurredColour, 100, 200) #for colour 
        #processes and outputs an image, 100 200 is the ratio for acceptable edge gradation 
        imgOutlinedBlackWhite = cv2.Canny(imgBlurredBlackWhite, 100, 200) #for black and white
        imgOutlinedGrayscale = cv2.Canny(self.gimg, 100, 200)
        #so that we can merge all three together to get better acuracy of the image

        imgOutlinedTemp = cv2.addWeighted(imgOutlinedBlackWhite,1,imgOutlinedColour,1,0) #merges two photos together
        imgOutlined = cv2.addWeighted(imgOutlinedTemp,1,imgOutlinedGrayscale,1,0)#merges a third to it
        # imgOutlined = cv2.bitwise_not(imgOutlined)
        self.eimg = imgOutlined


