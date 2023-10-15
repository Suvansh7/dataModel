import numpy as np
import matplotlib.pyplot as mlt
from PIL import Image
from crop import sheet1,sheet2
from locating import locate1

imgc=0
for i in range(2):
    for j in range(1):
        imgc=imgc+1
        img=np.array(Image.open(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\sheet{i+1}\\{j+1}.jpeg"))
        # img = img.sum(2)/(255*3) # convert it intop greyscale
        if(i==0):
            cropped=sheet1(img)
        elif(i==1):
            cropped=sheet2(img)
        else:
            cropped=[]

        
        locate1(cropped,imgc)