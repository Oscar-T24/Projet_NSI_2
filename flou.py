from PIL import Image
# NE FONCTIONERA PAS AVEC UNE IMAGE JPEG
# CREE UNE IMAGE FLOUTÉE E FAISANT LA MOYENNE DES PIXELKS ENVIRONNNANTS

image = Image.open('poisson.png')
taille_init = (image.width,image.height)
image = image.resize((round(taille_init[0]/3),round(taille_init[1]/3)))

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
    
    for e in range(8,image.width-8):
        for e2 in range(8,image.height-8):
            liste_rgb = []         
            for voisin_x in range(e-8,e+9,4):
                for voisin_y in range(e2-8,e2+9,4):
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

            moyenne_R = round(moyenne_R / len(liste_rgb)) # 64 pixels qui onnt été choisis
            moyenne_G = round(moyenne_G / len(liste_rgb))
            moyenne_V = round(moyenne_V / len(liste_rgb))
            # ----------------------------------------------------------------------------------------
            #print('moyennnes de chaque 9 pixel',moyennes)
            '''
            for voisin_x in range(e-6,e+6):
                for voisin_y in range(e2-6,e2+6):
                    rgb_im_final.putpixel((voisin_x, voisin_y), (moyenne_R,moyenne_G,moyenne_V, 0))
            '''
            """
            for voisin_x in range(e-8,e+9,4):
                for voisin_y in range(e2-8,e2+9,4):
                    rgb_im_final.putpixel((voisin_x, voisin_y), (moyenne_R,moyenne_G,moyenne_V, 24))
            """
            rgb_im_final.putpixel((voisin_x, voisin_y), (moyenne_R,moyenne_G,moyenne_V, 24))

    rgb_im_final.show()
    rgb_im.show()
    
flou2(image)