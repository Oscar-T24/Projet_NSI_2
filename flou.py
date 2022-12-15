from PIL import Image
# NE FONCTIONERA PAS AVEC UINE IMAGE SAS FOND(pour les PNG)

image = Image.open('Capture d’écran 2022-12-15 à 19.53.18.png')

image = image.resize((300,300))

def flou(image,pixels):
    '''
    pixels = nombre de pixels en longeur et largeur
    '''
    taille_ini = (image.width,image.height)
    image = image.resize((pixels,pixels))
    rgb_im = image.convert('RGB')
    for e in range(0,image.width):
        for e2 in range(0,image.height):
            r, g, b= rgb_im.getpixel((e, e2))
            rgb_im.putpixel( (e, e2), (g, 255-r, b, 0) )
    rgb_im = rgb_im.resize(taille_ini)
    rgb_im.show()

flou(image,200)

def flou2(image):
    '''
    pixels = nombre de pixels en longeur et largeur
    '''
    taille_ini = (image.width,image.height)
    rgb_im = image.convert('RGB')
    
    for e in range(0,image.width-1):
        for e2 in range(0,image.height-1):
            moyennes = 0
            liste_rgb = []
            for voisin_x in range(e-1,e+2):
                for voisin_y in range(e2-1,e2+2):
                    r, g, b = rgb_im.getpixel((voisin_x,voisin_y))
                    liste_rgb.append([r,g,b])
            # AJOUTER ICI UNE PARTIE QUI FAITT LA MOYENNE DE CHAQUE COMPOSANT RGB DES 8 PIXELS ET RENVOI 9 TUPLES À REINSERER
            incrementation = 0     
            # PARTIE D'ECRITURE DES PIXELS      
            for voisin_x in range(e-1,e+2):
                for voisin_y in range(e2-1,e2+2):                   
                    rgb_im.putpixel((voisin_x, voisin_y), (moyennes[incrementation],moyennes[incrementation], moyennes[incrementation], 0))
                    incrementation += 1
            
    rgb_im = rgb_im.resize(taille_ini)
    rgb_im.show()
flou2(image)