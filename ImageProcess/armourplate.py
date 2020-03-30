import cv2
import numpy as np 
import matplotlib.pyplot as plt 
if __name__=='__main__':
    img=cv2.imread("robot.jpg")
    img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_COMPLEX 
    # lower mask (0-10)
    lower_red = np.array([0,150,200])
    upper_red = np.array([10,255,255])
    mask = cv2.inRange(img_hsv, lower_red, upper_red)

# set my output img to zero everywhere except my mask
    output_img = img.copy()
    output_img[np.where(mask==0)] = 0
    imgray = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours : 
        approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)   
    # Used to flatted the array containing 
    # the co-ordinates of the vertices. 
        n = approx.ravel() 
        cv2.drawContours(output_img, [approx], -1, (0,255,0), 3)
        i = 0  
        ar=np.zeroes[]
        print(n)
        for j in n : 
            if(i== 0): 
                x = n[i] 
                y = n[i + 1] 
            i=i+1     
  
    newsize = (1000, 1000) 
    im1 = cv2.resize(output_img,newsize) 
    cv2.imshow("RED",im1)
    cv2.waitKey(0)