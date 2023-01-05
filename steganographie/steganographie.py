from cache_image_V4 import cache_image 
from retrouve_image_v4 import retrouve_image
from PIL import Image
import time

im1 = Image.open('images/9.jpeg')
im2 = Image.open('images/10.png')
# faire un script qui donne une pop up pour selectionner une image dans 
# le catalogue ou qui passe par openAI pour génerer une image

def main():
    #ajouter un menu
    #cache_image OU retrouve_image en fonction de la demande de l'utilisateur
    cache_image(im1,im2,5)
    image_fusion = Image.open('images/fusion.png')
    time.sleep(2)
    retrouve_image(image_fusion,5)

main()