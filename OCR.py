import easyocr
import numpy as np
import cv2
import sys
import os
import imageio
import matplotlib.cbook as cbook 
import matplotlib.image as image 
import matplotlib.pyplot as plt 



def main():
    print("Starting...")

    #spagetti
    imagePath = r".\inputs\tests"
    inDir = r'C:/Users/cckit/Desktop/ocr/inputs/GoodFrames'
    idk = r'C:\Users\cckit\Desktop\ocr\inputs\GoodFrames'
    outDir = r'C:\Users\cckit\Desktop\ocr\outputs\GoodFrames'

    
    
    #START LOOP HERE

    

    print("curr directory is ")
    print(os.getcwd())

    reader = easyocr.Reader(['en'])

    badIms = []
    
    for picture in os.listdir(inDir):

        
        img = idk + "\\" + picture
        #img = "C:\\Users\\cckit\\tests\\" + picture

        print(img)
        currImg = cv2.imread(img)

        if(currImg is None):
            badIms.append(picture)
            continue
        
        
        height = currImg.shape[0]
        width = currImg.shape[1]

        hRange = round(height * .20)
        wRange = width * .20

        sWidth = round(width-wRange)
        
        smolImage = currImg[0:hRange, sWidth:(width-1)]
        
        
        

        
        result = reader.readtext(smolImage)
    
        try:
            frameNumStr = result[0][1]
        except:
            cv2.imshow("whatever", currImg)
            cv2.moveWindow("whatever", 40,30)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            frameNumStr = input("Correction: ")

    
        if(not frameNumStr.isdigit()):
            
            cv2.imshow("whatever", smolImage)
            cv2.moveWindow("whatever", 40,30)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            frameNumStr = input("Correction: ")
        
        
        
        print(frameNumStr)
    

        
        filename = "ProjectS_" + frameNumStr + ".jpg"
        cv2.imwrite(filename, currImg)
        
    print("The bad frames are: ")
    print("")
    print (badIms)  
    print("Done")



if __name__ == "__main__":
    # execute only if run as a script
    main()
