import PIL
from PIL import Image

image = Image.open('images/6.png').convert('RGB')

def niveaux_de_gris(image):
    '''
    image --> image
    renvoie une image en noir et blanc
    '''
    lar,lon = image.width , image.height
    for x in range (lar):
        for y in range (lon):
            r,g,b = image.getpixel((x,y))
            moyenne_gris = round((r+g+b)/3)
            image.putpixel((x,y),(moyenne_gris,moyenne_gris,moyenne_gris))
    image.save('outputs/niveaux_de_gris.png')
    image.show()
            

niveaux_de_gris(image)