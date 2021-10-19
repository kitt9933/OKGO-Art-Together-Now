import numpy as np
import cv2
import sys
import os

#1261 - 1450 test range
print("Starting...")

inDir = r"C:\Users\cckit\Desktop\idk"
inDirF = r"C:/Users/cckit/Desktop/idk"



for picture in os.listdir(inDir):


    fileName = inDirF + "\\" + picture
    image = cv2.imread(fileName, 1)

    #color boundaries [B, G, R]
    lower = [0, 0, 0]
    upper = [100, 100, 100]

    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    ret,thresh = cv2.threshold(mask, 40, 255, 0)
    #if (cv2.__version__[0] > 3):
    #contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #else:
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(output, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)

        # draw the biggest contour (c) in green
        cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),2)

        crop = image[y:y+h,x:x+w]

    # show the images
    #np.hstack([image, output])
    #cv2.imshow("Result", crop)

    #cv2.waitKey(0)
    
    writeIm = "cropped_" + picture
    cv2.imwrite(writeIm, crop)
