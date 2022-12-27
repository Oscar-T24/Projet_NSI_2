from PIL import Image, ImageFilter
import statistics
# NE FONCTIONERA PAS AVEC UNE IMAGE JPEG
# CREE UNE IMAGE FLOUTÉE E FAISANT LA MOYENNE DES PIXELKS ENVIRONNNANTS

image = Image.open('images/6.png')
taille_init = (image.width,image.height)

def flou(image,rayon): 
    '''
    pixels = nombre de pixels en longeur et largeur
    img(png), int(pixels) -> img(png, floutée)
    fait pour chaque pixel la moyene du pixel et de celle des 8 pixels avoisinants
    '''
    #taille_ini = (image.width,image.height)
    rgb_im = image.convert('RGB') # on coverti en RGB pour maipuler les composantes vertes, rouges et blueus
    rgb_im_final = rgb_im.copy() # on crée une image qui sera modifiée ; l'autre initiale est utilisée comme guide

    moyenne_R = 0
    moyenne_G = 0
    moyenne_V = 0
    
    for x in range(rayon,image.width-(rayon+1)):
        for y in range(rayon,image.height-(rayon+1)):

    # ------------------------PARTIE PARCOURS --------------------------------------------------------

    # PARCOUR DE CHAQUE PIXEL : AMBIGUITÉ  : PREND ON LE MOYENNE DE CHAQUE PIXEL OU E FAISANT UN SAUT DE CARRÉ POUR ÉVITER DE FAIRE LA MOYENNE D PIXELS PLUSIEURS FOIS ?
            liste_rgb = [0,0,0]        
            comptage = 0
            for voisin_x in range(x-rayon,x+(rayon),rayon):
                for voisin_y in range(y-rayon,y+(rayon),rayon):
                    r, g, b = rgb_im.getpixel((voisin_x,voisin_y))
                    liste_rgb[0] += r
                    liste_rgb[1] += g
                    liste_rgb[2] += b
                    comptage += 1

            # on obtient une liste de 9 élements(chaque element ayant une composante RGB)

            # ------------------------PARTIE MOYENNE DE CHAQUE COMPOSANNT ----------------------------
            moyenne = [round((liste_rgb[i])/comptage) for i in range(3)]
            '''
            moyenne_R = round(liste_rgb[0] / comptage) 
            moyenne_G = round(liste_rgb[1] / comptage)
            moyenne_V = round(liste_rgb[2] / comptage)
            '''
            # ----------------------------------------------------------------------------------------
            #print('moyennnes de chaque 9 pixel',moyennes)
            
            rgb_im_final.putpixel((x, y), (moyenne[0],moyenne[1],moyenne[2]))

    rgb_im_final.show()
    rgb_im.show()
    
    
flou(image,8)

# CETTE FONCTION ABOUTIE A FAIRE LE FILTRE BOXBLUR DE LA LIBRAIRIE PIL

# Opens a image in RGB mode
im = Image.open('images/6.png')

# Blurring the image
im1 = im.filter(ImageFilter.BoxBlur(4))

# Shows the image in image viewer
im1.show()