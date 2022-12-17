from PIL import Image
# NE FONCTIONERA PAS AVEC UINE IMAGE SAS FOND(pour les PNG)

image = Image.open('chien.png')
taille_init = (image.width,image.height)
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

#flou(image,200)

def flou2(image): # Ajouter un facteur de floutage
    '''
    pixels = nombre de pixels en longeur et largeur
    '''
    #taille_ini = (image.width,image.height)
    rgb_im = image.convert('RGB')
    rgb_im_final = rgb_im.copy()
    moyenne_R = 0
    moyenne_G = 0
    moyenne_V = 0
    
    for e in range(4,image.width-3):
        for e2 in range(4,image.height-3):
            liste_rgb = []         
            for voisin_x in range(e-2,e+4,2):
                for voisin_y in range(e2-2,e2+4):
                     # loiste rgb d'un des 9 pixels
                    r, g, b = rgb_im.getpixel((voisin_x,voisin_y))
                    liste_rgb.append([r,g,b])
            #print('liste des 24 pixels avoisinnnants',liste_rgb,'longeur',len(liste_rgb))
            # LONGUEUR TOTALE : carré de 25 pixels
            # ------------------------PARTIE MOYENNE DE CHAQUE COMPOSANNT ----------------------------
            for e4 in liste_rgb:
                moyenne_R += e4[0] 
                moyenne_G += e4[1]
                moyenne_V += e4[2]

            moyenne_R = round(moyenne_R / 25)
            moyenne_G = round(moyenne_G / 25)
            moyenne_V = round(moyenne_V / 25)
            # ----------------------------------------------------------------------------------------
            #print('moyennnes de chaque 9 pixel',moyennes)
            '''
            for voisin_x in range(e-6,e+6):
                for voisin_y in range(e2-6,e2+6):
                    rgb_im_final.putpixel((voisin_x, voisin_y), (moyenne_R,moyenne_G,moyenne_V, 0))
            '''
            rgb_im_final.putpixel((e, e2), (moyenne_R,moyenne_G,moyenne_V, 0))
    rgb_im_final.show()
    rgb_im.show()
    
flou2(image)
image.show()