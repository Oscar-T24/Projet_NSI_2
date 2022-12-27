from cache_image import binR, decimL
from PIL import Image

image = Image.open('images/4+7.png').convert('RGB')

def retrouve_image(image):
    '''
    prend en argument une image fusionnnée selon le script cache_image
    et renvoi les deux images approximatives originales (a quelques erreur pres)
    '''
    for x in range(image.width):
        for y in range(image.height):



retrouve_image(image)