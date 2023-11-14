def locate1(arr,imgc,where):
    from PIL import Image
    c=where
    for i in arr:
        im=Image.fromarray(i)
        im.save(f"C:\\Users\\Lenovo\\Desktop\\MiniProject\\data\\{c+1}\\{c+1}_{imgc-1}.jpeg")
        c=c+1
    return 0