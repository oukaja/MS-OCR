try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def cropping_id_card(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    image = Image.open(filename)
    box = (735, 14, 1243, 333)
    cropped_image = image.crop(box)
    cropped_image.save(path + 'cropped_' + filename.filename)
    return path, path + 'cropped_' + filename.filename


def cropping_id_card_detail(path, filename):
    """
    When an image is cropped, a rectangular region inside the image is selected and retained while everything else outside the region is removed.
    """
    path, filename = cropping_id_card(path, filename)
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


def ocr_id_card(path, filename):
    """
    This function will handle the core OCR processing of id card images.
    """
    cropping_id_card_detail(path, filename)
    info = {'first_name': ocr_core(path + 'fisrt_name_image.jpg'),
            'last_name': ocr_core(path + 'last_name_image.jpg'),
            'bd': ocr_core(path + 'bd_image.jpg'),
            'ville': ocr_core(path + 'ville_image.jpg'),
            'id_num': ocr_core(path + 'id_num_image.jpg'),
            'validity': ocr_core(path + 'validity_image.jpg')
            }
    return info

