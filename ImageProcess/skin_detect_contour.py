import numpy as np
import cv2
if __name__=='__main__':
    min_HSV = np.array([0, 58, 30], dtype = "uint8")
    max_HSV = np.array([33, 255, 255], dtype = "uint8")
    im = cv2.imread("Man.jpg")
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    imHSV=cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    skinRegionHSV = cv2.inRange(imHSV, min_HSV, max_HSV)
    skinHSV = cv2.bitwise_or(im, im, mask = skinRegionHSV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(skinHSV, contours, -1, (0,255,0), 3)
    cv2.imshow("Contour image",skinHSV)
    cv2.waitKey(5000)
    cv2.imshow("Skin image",skinRegionHSV)
    cv2.waitKey(5000)