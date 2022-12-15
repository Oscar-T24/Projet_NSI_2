'https://github.com/Oscar-T24/Projet_NSI_2'

# Faire une fonction qui retourne l'image avec l'utilisation de la librairie pillow

import PIL
from PIL import Image

def miroir(image):
    # On ouvre l'image
    img = Image.open(image)
    # On récupère la taille de l'image
    largeur, hauteur = img.size
    # On crée une nouvelle image
    img2 = Image.new('RGB', (largeur, hauteur))
    # On parcourt l'image
    for x in range(largeur):
        for y in range(hauteur):
            # On récupère la couleur du pixel
            couleur = img.getpixel((x, y))
            # On la place dans la nouvelle image
            img2.putpixel((largeur - x - 1, y), couleur)
    # On sauvegarde l'image
    img2.save('miroir.png')

# On appelle la fonction
miroir('image.png')