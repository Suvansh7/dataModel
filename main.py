import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from crop import sheet1,sheet2,sheet
from locating import locate1
from crop_detection import detect

imgc=0

def set_of_3():
    for i in range(2):
        for j in range(1):
            # imgc=imgc+1
            img=np.array(Image.open("C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\sheet1\\1.jpeg"))
            # img = img.sum(2)/(255*3) # convert it intop greyscale
            if(i==0):
                cropped=sheet1(img)
            elif(i==1):
                cropped=sheet2(img)
            else:
                cropped=[]

        
            locate1(cropped,1,0)

def single_sheet_set():

    for i in range(4):
        img=np.array(Image.open(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\collection\\{i+1}.jpg"))
        detect(img)

def scanned_sheet():
    for i in range(4):
        img=np.array(Image.open(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\collection\\{i+1}.jpg"))
        sheet(img)


# single_sheet_set()
img=np.array(Image.open("C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\sheet1\\1.jpeg"))
img=img.sum(2) / (255*3)
# print(img)
set_of_3()
plt.imshow(img)
plt.show()