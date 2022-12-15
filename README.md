
# 6 Fonctions à faire
https://github.com/Oscar-T24/Projet_NSI_2


niveaux_de_gris(image) => Jad
miroir(image) => Arno
flou(image) => Oscar
fonctions de stéganographie : cache_image(im1, im2) et
retrouve_image(image)
et une fonction de votre choix.


import PILLOW

# Utilisation du module pillow
https://apprendrepython.com/comment-utiliser-pillow-pil-python-imaging-library/


from PIL import Image, ImageFilter

im = Image.open('data/src/lenna_square.png')

print(im.format, im.size, im.mode)
# PNG (512, 512) RGB


Par exemple, le traitement de la conversion en niveaux de gris (convert(‘L’)), de la rotation de 90 degrés (rotate(90)) et du flou gaussien (filter()) est effectué.

new_im = im.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())

Affichez les images avec le logiciel par défaut du système d’exploitation.

Enregistrez l’image.

new_im.save('data/dst/lenna_square_pillow.jpg', quality=95)



