from PIL import Image
# POUR CONVERTIR DES DECIMAUX EN BINAIRE ET VICE VERSA ON PEUX SIMPLEMENT UTILISER int() et bin()

im1 = Image.open('images/9.png').convert('RGB')
im2 = Image.open('images/9.png').convert('RGB')



def cache_image(im1,im2):
    '''
    img,img --> img
    cache l'image 2 dans l'image 1 par scetanographie
    '''
    if im1.size > im2.size :
        im_final = Image.new('RGB',(im2.width,im2.height))
        im1.resize((im2.width,im2.height))
    else :
        im_final = Image.new('RGB',(im1.width,im1.height))
        im2.resize((im1.width,im1.height))
    # pour rappel, chaque composante d'un pixel est codée sur 8 bits : de 0 à 255 variantes d'une couleur
    for x in range(im1.width):
        for y in range(im1.height):
            r, v, b = im1.getpixel((x,y))
            r2,v2,b2 = im2.getpixel((x,y))
            pixel1 = [binR(r,5),binR(v,5),binR(b,5)] # on garde les 5 plus grands bits du pixel 1
            pixel2 = [binR(r2,3),binR(v2,3),binR(b2,3)] # o garde les 3 plus grands bits du pixel 2
            pixel_final = [decimL(int(pixel1[i]+pixel2[i])) for i in range(3)] # on assemble les 5 premiers bits du pixel 1 avec les 3 premier bits du pixel 2          # option if pixel1[i] != '' and pixel2[i] != ''
            #try :
            im_final.putpixel((x,y),tuple(pixel_final))
            #except TypeError:
                #pass
    im_final.show()
         
def binR(decimal, chiffres_sigificatifs):
    '''
    int --> int
    renvoi la valeur décimale d'un chiffer bianire
    '''
    resultat = ''
    while decimal != 0 :
        resultat += str(decimal % 2)
        decimal = decimal // 2
    resultat = resultat[::-1]
    return resultat[0:chiffres_sigificatifs]

def decimL(binaire):
    i = 0
    decimal = 0
    while binaire != 0:
        bit = binaire % 10 #determine si le digit est un 0 ou un 1
        decimal += bit * pow(2,i)
        binaire //= 10
        i += 1
    return decimal

cache_image(im1,im2)

