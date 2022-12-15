# Projet 2 - Manipulation d'images
# ===
# 
# Exemples d'utilisation de la librairie PIL

from PIL import Image

# Chargement et affichage d'une image

image = Image.open('chien.png')
image.show()


# Affichage de la taille de l'image et de la valeur du pixel au centre

print('taille =', image.width, image.height)

largeur, hauteur = image.width, image.height
cx = int(largeur/60)
cy = int(hauteur/60)

p = image.getpixel((cx, cy))
print('valeur RGB du pixel au centre =', p)

# Extraction et affichage d'une sous-image de 100x100 pixels au centre

centre = image.crop((cx-50, cy-50, cx+50, cy+50))
centre.show()

# Collage de la sous-image dans le coin supérieur gauche de l'image de départ

image.paste(centre,(0, 30, 10, 40))
image.show()

# Affectation des pixels au centre de l'image

for i in range(-50, 50):
    for j in range(-50, 50):
        image.putpixel((int(largeur/2) + i, int(hauteur/2) + j), (0, 0, 250))

image.show()
