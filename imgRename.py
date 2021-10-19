import numpy as np
import sys
import os




def main():

    print("Starting...")

    print("curr directory is ")
    print(os.getcwd())

    inDir = r'C:/Users/cckit/Desktop/ocr/inputs/irt'
    idk = r'C:\Users\cckit\Desktop\ocr\inputs\irt'


    for picture in os.listdir(inDir):

        img = idk + "\\" + picture
        userNum = input("Number: ")
        dst = idk + "\\ProjectW_00" + userNum + ".jpg"

        os.rename(img,dst)

        

    print("Done")
   
if __name__ == "__main__":
    # execute only if run as a script
    main()
