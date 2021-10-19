from PIL import Image
import cv2
import sys
import os

def main(): 
    #image = Image.open("ProjectV_000134.jpg")

    img = cv2.imread('ProjectV_000134.jpg',0)
    #bw = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    
    _,thresh = cv2.threshold(img,50,100,cv2.THRESH_BINARY_INV)


    
    
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]


    #img = cv2.drawContours(img, contours, -1, (0,255,0), 3)

 

    #epsilon = 0.1*cv.arcLength(cnt,True)
    #approx = cv.approxPolyDP(cnt,epsilon,True)

    

    
    x,y,w,h = cv2.boundingRect(cnt)

    crop = img[y:y+h,x:x+w]
    cv2.imshow('img',crop)
    cv2.waitKey(0) 
  
    #closing all open windows 
    cv2.destroyAllWindows() 


if __name__ == "__main__":
    # execute only if run as a script
    main()
