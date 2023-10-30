def detect(img):
    import numpy as np
    import matplotlib.pyplot as plt
    from icecream import ic

    img = img.sum(2) / (255*3)
    print(img.shape)

    flag=False
    geo=img.shape
    for x in range(5,500):
        for y in range(5,200):
            if(img[y,x]<0.6):
                quad1=(y,x)
                ic()
                flag=True
                break
            if(flag):
                break
        if(flag):
            break
    # flag=False
    # for x in range(-50,-250,-1):
    #     for y in range(20,100):
    #         if(img[y,x]<0.5):
    #             quad2=(y,x+geo[1])
    #             print(quad2)
    #             flag=True
    #             break
    #         if(flag):
    #             break
    #     if(flag):
    #         break

    # flag=False
    # for x in range(50,250):
    #     for y in range(-20,-150,-1):
    #         if(img[y,x]<0.6):
    #             quad3=(y+geo[0],x)
    #             flag=True
    #             break
    #         if(flag):
    #             break
    #     if(flag):
    #             break
    
    flag=False
    for x in range(-5,-500,-1):
        for y in range(-5,-250,-1):
            if(img[y,x]<0.6):
                quad4=(y+geo[0],x+geo[1])
                flag = True
                break
            if(flag):
                break
        if(flag):
            break

    print(quad1,quad4)
    img = img[quad1[0]:quad4[0],quad1[1]:quad4[1]]

    

    plt.imshow(img)
    plt.show()

