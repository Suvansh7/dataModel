def locate1(arr,imgc,where):
    from PIL import Image
    import numpy as np

    c=where
    orig = Image.open("C:\\Users\\Lenovo\\Desktop\\MiniProject\\set\\sheet1\\0.jpg")
    for i in arr:
    
        im=Image.fromarray(i)
        im = im.convert(orig.mode)
        im.save(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\data\\{c+1}\\{c+1}_{imgc+100}.jpeg")
        c=c+1
    return 0