def detect(img):
    import numpy as np
    import matplotlib.pyplot as plt

    img = img.sum(2) / (255*3)
    print(img)


    plt.imshow(img)
    plt.show()

