from PIL import Image
# NE FONCTIONERA PAS AVEC UNE IMAGE JPEG
# CREE UNE IMAGE FLOUTÉE E FAISANT LA MOYENNE DES PIXELKS ENVIRONNNANTS

image = Image.open('images/poisson.png')
taille_init = (image.width,image.height)
image = image.resize((round(taille_init[0]/3),round(taille_init[1]/3))) # resize l'image pour rendre le processus plus rapide


def flou(image): 
    '''
    pixels = nombre de pixels en longeur et largeur
    img(png) -> img(png, floutée)
    fait pour chaque pixel la moyene du pixel et de celle des 8 pixels avoisinants
    '''
    #taille_ini = (image.width,image.height)
    rgb_im = image.convert('RGB') # on coverti en RGB pour maipuler les composantes vertes, rouges et blueus
    rgb_im_final = rgb_im.copy() # on crée une image qui sera modifiée ; l'autre initiale est utilisée comme guide

    moyenne_R = 0
    moyenne_G = 0
    moyenne_V = 0
    
    for x in range(1,image.width):
        for y in range(1,image.height):

    # ------------------------PARTIE PARCOURS --------------------------------------------------------

    # PARCOUR DE CHAQUE PIXEL : AMBIGUITÉ  : PREND ON LE MOYENNE DE CHAQUE PIXEL OU E FAISANT UN SAUT DE CARRÉ POUR ÉVITER DE FAIRE LA MOYENNE D PIXELS PLUSIEURS FOIS ?
            liste_rgb = []         
            for voisin_x in range(x-1,x+2):
                for voisin_y in range(y-1,y+2):
                    r, g, b = rgb_im.getpixel((voisin_x,voisin_y))
                    liste_rgb.append([r,g,b])

            # on obtient une liste de 9 élements(chaque element ayant une composante RGB)

            # ------------------------PARTIE MOYENNE DE CHAQUE COMPOSANNT ----------------------------

            # A SYNNTHETISER 

            for rgb in liste_rgb:
                moyenne_R += rgb[0] 
                moyenne_G += rgb[1]
                moyenne_V += rgb[2]
        
            moyenne_R = round(moyenne_R / len(liste_rgb)) 
            moyenne_G = round(moyenne_G / len(liste_rgb))
            moyenne_V = round(moyenne_V / len(liste_rgb))
            # ----------------------------------------------------------------------------------------
            #print('moyennnes de chaque 9 pixel',moyennes)
            
            rgb_im_final.putpixel((x, y), (moyenne_R,moyenne_G,moyenne_V, 9))

    rgb_im_final.show()
    rgb_im.show()
    
flou2(image)