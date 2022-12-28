##----- Importation des Modules -----##
from PIL import Image

##----- Définition des Fonctions -----##
def masque(n):
    """Masquage des pixels de poids faible."""
    return n & 0b11110000

def decale(n, dec=4):
    """Remplace les pixels de poids faible par les pixels de poids fort."""
    return n >> dec  # n >> 4 = n//16

##----- Informations sur les images d'origine -----##
im1 = Image.open('images/8.jpg') # image qui restera visible
im2 = Image.open('images/9.jpeg') # image à cacher
l, h = im1.size

##----- Conception de la nouvelle image -----##
im_resultat = Image.new('RGB', (l, h))

for x in range(l):
    for y in range(h):
        r1, v1, b1 = im1.getpixel((x, y))
        r1, v1, b1 = masque(r1), masque(v1), masque(b1)
        r2, v2, b2 = im2.getpixel((x, y))
        r2, v2, b2 = decale(r2), decale(v2), decale(b2)
        im_resultat.putpixel((x,y), (r1+r2, v1+v2, b1+b2))
		# r1 + r2 = les 4 bits de poids fort de r1initial à gauche,
		# les 4 bits de poids forts de r2initial à droite

##-----Finalisation-----##
im_resultat.show()