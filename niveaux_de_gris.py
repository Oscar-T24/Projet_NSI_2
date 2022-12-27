import PIL
from PIL import Image


def niveaux_de_gris(image):
    '''
    image --> image
    renvoie une image en niveau de gris
    '''
    lar,lon = image.width , image.height
    for x in range (lar):
        for y in range (lon):
            r,g,b = image.getpixel((x,y))
            moyenne_gris = round((r+g+b)/3)
            image.putpixel((x,y),(moyenne_gris,moyenne_gris,moyenne_gris))
    image.show()
            

image = Image.open('images/9.png')
niveaux_de_gris(image)