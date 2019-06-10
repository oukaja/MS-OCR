try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
from matplotlib import pyplot as plt
import numpy as np
import cv2


def avoid_noise(path, filename):
    img = cv2.imread(path + filename.filename)
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    grayImage = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path + 'graylevel_' + filename.filename,grayImage)
    return None

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def cropping_pay(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    image = Image.open( filename)
    ste_name = (158, 294, 255, 314)
    ste_name_image = image.crop(ste_name)
    ste_name_image.save(path + 'ste_name_image.jpg')
    ###
    cnss = (508, 332, 605, 353)
    cnss_image = image.crop(cnss)
    cnss_image.save(path + 'cnss_image.jpg')
    ###
    sba = (318, 444, 390, 462)
    sba_image = image.crop(sba)
    sba_image.save(path + 'sba_image.jpg')
    ###
    mutuelle_cnss = (317, 465, 384, 481)
    mutuelle_cnss_image = image.crop(mutuelle_cnss)
    mutuelle_cnss_image.save(path + 'mutuelle_cnss_image.jpg')
    ###
    revenue_net = (300, 482, 380, 500)
    revenue_net_image = image.crop(revenue_net)
    revenue_net_image.save(path + 'revenue_net_image.jpg')
    return 'Done'


def ocr_pay(path, pay):
    """
    This function will handle the core OCR processing of id card images.
    """
    cropping_pay(path, pay)
    info = {'ste_name': ocr_core(path + 'ste_name_image.jpg'),
            'cnss': str(ocr_core(path + 'cnss_image.jpg')).replace(' ',''),
            'sba': str(ocr_core(path + 'sba_image.jpg')).replace(' ',''),
            'mutuelle_cnss': str(ocr_core(path + 'mutuelle_cnss_image.jpg')).replace(' ',''),
            'revenue_net': str(ocr_core(path + 'revenue_net_image.jpg')).replace(' ',''),
            }
    return info
