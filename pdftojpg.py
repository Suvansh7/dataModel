import fitz  
from PIL import Image

def pdf_to_jpg(pdf_path):

    images=[]

    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]

    
        pixmap = page.get_pixmap()

    
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        rotated_image = image.rotate(180)

        jpg_image = Image.new("RGB", rotated_image.size)
        jpg_image.paste(rotated_image)
        images.append(jpg_image) 


    pdf_document.close()
    return images


pdf_path = 'C:\\Users\\Utkar\\OneDrive\\Desktop\\Miniproject\\dataModel\\SetOf3.pdf'

images = pdf_to_jpg(pdf_path)


