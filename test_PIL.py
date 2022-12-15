# Projet 2 - Manipulation d'images
# ===
# 
# Exemples d'utilisation de la librairie PIL

from PIL import Image

# Chargement et affichage d'une image

image = Image.open('chien.png')
image.show()

# The error is because you are trying to open a non-image file with Image.open().

# If your goal is to move the file from one folder to another then I would suggest you use

# os.rename(SourceFileName,TargetFileName)

# If not, consider filtering your input file before calling Image.open to specific extensions that you would like to access, say like:-

# ext=['jpg','png','gif']
# for filename in os.listdir(image_folder):
#     if filename[-3:] in ext:
#         img= Image.open(f'{image_folder}{filename}')
#         img.save(f'{output_folder}{filename}', 'png')
#     print ('all done!')

# Hope that helps


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

image.paste(centre,(0, 0, 100, 100))
image.show()

# Affectation des pixels au centre de l'image

for i in range(-50, 50):
    for j in range(-50, 50):
        image.putpixel((int(largeur/2) + i, int(hauteur/2) + j), (0, 0, 250))

image.show()
