# import fitz  
# from PIL import Image

# def pdf_to_jpg(pdf_path):

#     images=[]

#     pdf_document = fitz.open(pdf_path)

#     for page_num in range(pdf_document.page_count):
#         page = pdf_document[page_num]

    
#         pixmap = page.get_pixmap()

    
#         image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

#         rotated_image = image.rotate(180)

#         jpg_image = Image.new("RGB", rotated_image.size)
#         jpg_image.paste(rotated_image)
#         images.append(jpg_image) 


#     pdf_document.close()
#     return images

# def locate(img_lst):

#     c=0
#     total,total2=0,0
#     for i in img_lst:
#         if (c<44):
#             im=Image.fromarray(i)
#             im.save(f"C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\set\\sheet1\\{c}.jpg")
#             c=c+1
#             total = c
#         elif(c<75):
#             im=Image.fromarray(i)
#             im.save(f"C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\set\\sheet2\\{c}.jpg")
#             c=c+1
#             total2=c
#         else:
#             im=Image.fromarray(i)
#             im.save(f"C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\set\\sheet3\\{c}.jpg")
#             c=c+1


# pdf_path = 'C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\SetOf3.pdf'

# images = pdf_to_jpg(pdf_path)
# locate(images)

import fitz  
from PIL import Image

def pdf_to_jpg(pdf_path):
    images = []

    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]

        pixmap = page.get_pixmap()

        # Convert the pixmap to bytes before creating a Pillow image
        image_data = pixmap.samples
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], image_data)

        rotated_image = image.rotate(180)

        jpg_image = Image.new("RGB", rotated_image.size)
        jpg_image.paste(rotated_image)
        images.append(jpg_image)

    pdf_document.close()
    return images

def locate(img_lst):
    c = 0
    total, total2 = 0, 0

    for i in img_lst:
        if c < 43:
            im = i  # Use the Pillow image directly
            im.save(f"C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\set\\sheet1\\{c}.jpg")
            c = c + 1
            total = c
        elif (c < 74):
            im = i  # Use the Pillow image directly
            im.save(f"C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\set\\sheet2\\{c}.jpg")
            c = c + 1
            total2 = c
        else:
            im = i  # Use the Pillow image directly
            im.save(f"C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\set\\sheet3\\{c}.jpg")
            c = c + 1

pdf_path = 'C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\SetOf3.pdf'
images = pdf_to_jpg(pdf_path)
locate(images)

