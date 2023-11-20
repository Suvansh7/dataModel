import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from crop import cp
from locating import locate1
from crop_detection import detect

imgc=0

def set_of_3():
    for i in range(42):
    
        img = np.array(Image.open(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\sheet1\\{i}.jpg"))
        img=img.sum(2) / (255*3)
        # plt.imshow(img)
        # plt.show()
        cropped = cp(img)
        
        locate1(cropped,1,0,i)

def single_sheet_set():

    for i in range(4):
        img=np.array(Image.open(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\collection\\{i+1}.jpg"))
        detect(img)

def scanned_sheet():
    for i in range(4):
        img=np.array(Image.open(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\collection\\{i+1}.jpg"))
        sheet(img)


# single_sheet_set()
# img=np.array(Image.open("C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\sheet1\\1.jpeg"))
# img=img.sum(2) / (255*3)
# print(img)
set_of_3()
# plt.imshow(img)
# plt.show()