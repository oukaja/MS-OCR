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


def cropping_paie(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    # avoid_noise(path, filename)
    image = Image.open(filename)
    num_cimr = (433,345,497,365)
    num_cimr_image = image.crop(num_cimr)
    num_cimr_image.save(path + 'num_cimr_image.jpg')
    ###
    matricule = (530,345,590,365)
    matricule_image = image.crop(matricule)
    matricule_image.save(path + 'matricule_image.jpg')
    
    date_debut = (215,390,307,408)
    date_debut_image = image.crop(date_debut)
    date_debut_image.save(path + 'date_debut_image.jpg')
    ###
    sit_fam = (320,390,420,408)
    sit_fam_image = image.crop(sit_fam)
    sit_fam_image.save(path + 'sit_fam_image.jpg')
    ###
    fonction = (525,385,695,408)
    fonction_image = image.crop(fonction)
    fonction_image.save(path + 'fonction_image.jpg')
    ###
    salaire_base = (643,1370,728,1389)
    salaire_base_image = image.crop(salaire_base)
    salaire_base_image.save(path + 'salaire_base_image.jpg')
    ###
    mois_paie = (105,345,190,363)
    mois_paie_image = image.crop(mois_paie)
    mois_paie_image.save(path + 'mois_paie_image.jpg')
    return 'Done' 




def ocr_paie(path, paie):
    """
    This function will handle the core OCR processing of id card images.
    """
    cropping_paie(path, paie)
    info = {'num_cimr': str(ocr_core(path + 'num_cimr_image.jpg')).replace(' ',''),
            'matricule': str(ocr_core(path + 'matricule_image.jpg')).replace(' ',''),
            'date_debut': str(ocr_core(path + 'date_debut_image.jpg')).replace(' ',''),
            'sit_fam': str(ocr_core(path + 'sit_fam_image.jpg')).replace(' ',''),
            'fonction': str(ocr_core(path + 'fonction_image.jpg')).replace(' ',''),
            'salaire_base': str(ocr_core(path + 'salaire_base_image.jpg')).replace(' ',''),
            'mois_paie': str(ocr_core(path + 'mois_paie_image.jpg')).replace(' ','')
            }
    return info
