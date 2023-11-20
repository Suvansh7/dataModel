import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
img = np.array(Image.open("C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\sheet1\\0.jpg"))   # converting image to array
img = img.sum(2) / (255*3)  # converting rgb to gray scale
img_updated = Image.fromarray(img)   # converting array to image
plt.imsave('C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\jjj2.jpeg', img_updated, cmap='gray')
# cv2.imwrite("C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\jjj.jpeg", img)
# img_updated.save("C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\jjj.jpeg")  # saving image
      