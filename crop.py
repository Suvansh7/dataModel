def cord(x,x_range,y,y_range,img):
    for x in range(x_range):
        for y in range(y_range):
            if img[x,y] < 0.8:
                print(img[x,y])
                q = (x,y)
                return(q)


def cp(img):
    import numpy as np
    import matplotlib.pyplot as plt

    q1 = cord(0,20,0,20,img)          
    print(q1)
    y1 = q1[0] - 4
    y2 = y1 + 117
    x1 =  q1[1] - 4
    x2 = x1 + 114

    lst = []
    for row in range(7):
        r = 2
        for column in range(5):
             
             imgg = img [ y1+6:y2-6 , x1+6:x2-6]
             lst.append(imgg)
            #  plt.imshow(imgg)
            #  plt.show()
             x1 = x1 + 114
             x2 = x2 + 114
             r = r + r
             

        y1 = y1 + 115
        y2 = y2 + 115
        x1 =  q1[1]
        x2 = x1 + 114
 

    imgg=img[q1[0]:q1[0]+108,q1[1]:q1[1]+110]
    return lst
    







# def sheet(img):
#     return 0

# def sheet1(img):
#     import numpy as np
#     import matplotlib.pyplot as plt
#     ll=[]
#     y=0
#     x=0
#     for row in range(7):
#         x=0
#         for column in range(5):
#             # temp_img=img[y:y+311,x:x+312]
#             temp_img=img[y+5:y+309-5,x+5:x+305-5] # in total m se center ki trf aaon
#             ll.append(temp_img)
#             x=x+305+10 # for margin
#         y=y+309+8 # for margin jump
#     return ll

# def sheet2(img):
#     import numpy as np
#     import matplotlib.pyplot as plt
#     ll=[]
#     y=58
#     x=91
#     for row in range(7):
#         x=91
#         for column in range(5):
#             # temp_img=img[y:y+311,x:x+312]
#             temp_img=img[y+5:y+309-5,x+5:x+305-5] # in total m se center ki trf aaon
#             ll.append(temp_img)
#             x=x+305+10 # for margin
#         y=y+309+8 # for margin jump
#     return ll

