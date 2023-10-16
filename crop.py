def sheet1(img):
    import numpy as np
    import matplotlib.pyplot as plt
    ll=[]
    y=58
    x=64
    for row in range(7):
        x=64
        for column in range(5):
            # temp_img=img[y:y+311,x:x+312]
            temp_img=img[y+5:y+309-5,x+5:x+305-5] # in total m se center ki trf aaon
            ll.append(temp_img)
            x=x+305+10 # for margin
        y=y+309+8 # for margin jump
    return ll

def sheet2(img):
    import numpy as np
    import matplotlib.pyplot as plt
    ll=[]
    y=58
    x=91
    for row in range(7):
        x=91
        for column in range(5):
            # temp_img=img[y:y+311,x:x+312]
            temp_img=img[y+5:y+309-5,x+5:x+305-5] # in total m se center ki trf aaon
            ll.append(temp_img)
            x=x+305+10 # for margin
        y=y+309+8 # for margin jump
    return ll

