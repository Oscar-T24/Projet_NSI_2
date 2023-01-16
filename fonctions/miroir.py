import PIL
from PIL import Image

def miroir(image):
    '''
    image --> image
    renvoie une image retournée horizontalement
    '''
    longueur, largeur = image.size
    # On récupère les pixels de l'image et on inverse l'image horizontalement
    pixels = [[image.getpixel((x, y)) for x in range(longueur)] for y in range(largeur)]
    pixels = [ligne[::-1] for ligne in pixels]
    image2 = Image.new('RGB', (longueur, largeur)) # On crée une image vide
    image2.putdata([pixel for ligne in pixels for pixel in ligne]) # On met les pixels dans l'image
    image2.save('outputs/miroir.png') # On sauvegarde l'image
    image2.show() # On affiche l'image

# On appelle la fonction
image = Image.open('images/6.png').convert('RGB')
miroir('images/6.png')
