'https://github.com/Oscar-T24/Projet_NSI_2'

# Faire une fonction qui retourne l'image avec l'utilisation de la librairie pillow

import PIL
from PIL import Image

def miroir(image):
    # On ouvre l'image
    img = Image.open(image)
    img = img.convert('RGB')
    longueur, largeur = img.size
    # On récupère les pixels de l'image et on inverse l'image horizontalement
    pixels = [[img.getpixel((x, y)) for x in range(longueur)] for y in range(largeur)]
    pixels = [ligne[::-1] for ligne in pixels]
    # On crée une nouvelle image
    img2 = Image.new('RGB', (longueur, largeur))
    # On met les pixels dans l'image
    img2.putdata([pixel for ligne in pixels for pixel in ligne])
    # On sauvegarde l'image
    img2.save('miroir.png')

# On appelle la fonction
miroir('chien.png')
