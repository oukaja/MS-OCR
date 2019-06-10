try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
from matplotlib import pyplot as plt
import numpy as np
import cv2
from hammock import Hammock as GendreAPI

gendre = GendreAPI("http://api.namsor.com/onomastics/api/json/gendre")

def get_gender(first_name, last_name):
    resp = gendre(first_name, last_name).GET()
    return resp.json().get('gender')


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def cropping_id_card_front(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    image = Image.open(filename)
    box = (735, 14, 1243, 333)
    cropped_image = image.crop(box)
    cropped_image.save(path + 'cropped_' + filename.filename)
    avoid_noise(path, 'cropped_' + filename.filename)
    return path, path + 'cropped_graylevel_cropped_' + filename.filename


def cropping_id_card_front_detail(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    path, filename = cropping_id_card_front(path, filename)
    image = Image.open(filename)
    fisrt_name = (14, 100, 190, 122)
    fisrt_name_image = image.crop(fisrt_name)
    fisrt_name_image.save(path + 'fisrt_name_image.jpg')
    ###
    last_name = (14, 140, 100, 165)
    last_name_image = image.crop(last_name)
    last_name_image.save(path + 'last_name_image.jpg')
    ###
    bd = (130, 161, 216, 187)
    bd_image = image.crop(bd)
    bd_image.save(path + 'bd_image.jpg')
    ###
    ville = (30, 200, 123, 230)
    ville_image = image.crop(ville)
    ville_image.save(path + 'ville_image.jpg')
    ###
    id_num = (365, 243, 438, 264)
    id_num_image = image.crop(id_num)
    id_num_image.save(path + 'id_num_image.jpg')
    ###
    validity = (150, 222, 232, 245)
    validity_image = image.crop(validity)
    validity_image.save(path + 'validity_image.jpg')
    return 'Done'


def cropping_id_card_back(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    image = Image.open(filename)
    box = (735, 14, 1243, 333)
    cropped_image = image.crop(box)
    cropped_image.save(path + 'cropped_' + filename.filename)
    avoid_noise(path, 'cropped_' + filename.filename)
    return path, path + 'cropped_graylevel_cropped_' + filename.filename


def cropping_id_card_back_detail(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    path, filename = cropping_id_card_back(path, filename)
    image = Image.open(filename)
    father_name = (62, 85, 240, 105)
    father_name_image = image.crop(father_name)
    father_name_image.save(path + 'father_name_image.jpg')
    ###
    mother_name = (55, 105, 185, 125)
    mother_name_image = image.crop(mother_name)
    mother_name_image.save(path + 'mother_name_image.jpg')
    ###
    adr = (65, 165, 465, 185)
    adr_image = image.crop(adr)
    adr_image.save(path + 'adr_image.jpg')
    ###
    gender = (409, 199, 428, 216)
    gender_image = image.crop(gender)
    gender_image.save(path + 'gender_image.jpg')
    ###
    cs_num = (110, 200, 190, 220)
    cs_num_image = image.crop(cs_num)
    cs_num_image.save(path + 'cs_num_image.jpg')
    return 'Done'


def ocr_id_card(path, cin_front, cin_back):
    """
    This function will handle the core OCR processing of id card images.
    """
    cropping_id_card_front_detail(path, cin_front)
    cropping_id_card_back_detail(path, cin_back)
    info = {'first_name': ocr_core(path + 'fisrt_name_image.jpg'),
            'last_name': ocr_core(path + 'last_name_image.jpg'),
            'bd': str(ocr_core(path + 'bd_image.jpg')).replace('.', '/'),
            'ville': ocr_core(path + 'ville_image.jpg'),
            'id_num': ocr_core(path + 'id_num_image.jpg'),
            'validity': str(ocr_core(path + 'validity_image.jpg')).replace('.', '/'),
            'father_name': ocr_core(path + 'father_name_image.jpg'),
            'mother_name': ocr_core(path + 'mother_name_image.jpg'),
            'adr': ocr_core(path + 'adr_image.jpg'),
            'gender': get_gender(ocr_core(path + 'fisrt_name_image.jpg'), ocr_core(path + 'last_name_image.jpg')),
            'cs': ocr_core(path + 'cs_num_image.jpg')
            }
    return info


def avoid_noise(path, filename):
    img = cv2.imread(path + filename)
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    grayImage = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path + 'cropped_graylevel_' + filename,grayImage)
    return None


if __name__ == "__main__":
    print(get_gender('OUKAJA', 'Youssef Mehdi'))