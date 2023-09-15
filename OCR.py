import pytesseract
from PIL import Image
import cv2
import numpy as np
from mapper import mapp

def readable(path):

    image = cv2.imread(path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image = cv2.resize(image,(800,1000))


    adaptive = cv2.adaptiveThreshold(image,200,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY,41,5)

    cv2.imshow('adapt',adaptive)

    cv2.imwrite('folder/enhanced_image.jpg',adaptive)

    cv2.waitKey(0)

def crop(path):

    image = cv2.imread(path)

    image = cv2.resize(image,(1300,800))

    orig = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray,(5,5),0)

    edged = cv2.Canny(blurred,30,50)


    contours, heiarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


    contours = sorted(contours, key= cv2.contourArea, reverse=True)



    for c in contours:

        p = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*p,True)

        if len(approx)==4:
            target = approx
            break

    approx = mapp(target)

    pts = np.float32([[0,0],[800,0],[800,800],[0,800]])

    op = cv2.getPerspectiveTransform(approx,pts)
    dst = cv2.warpPerspective(orig,op,(800,800))

    cv2.imshow('Scanned',dst)
    cv2.imwrite('folder/enhanced_image.jpg',dst)
    cv2.waitKey(0)


    return 'folder/enhanced_image.jpg'











if __name__=='__main__':

    readable('folder/20230114_172145.jpg')

    custom_config = r'--oem 1 --psm 6 -l pol+num'

    print(pytesseract.image_to_string('folder/enhanced_image.jpg',lang='Pol', config=custom_config))


