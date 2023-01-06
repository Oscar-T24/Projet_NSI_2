from PIL import Image


def masque_faibles(n,dec):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage: plus elle est grande, plus l'image aura de bits de poids forts
    out : un entier entre 0 et 255 ; sans bits de poids faibles
    """
    masque = 0b1111111100000000 >> dec # étape 1 : décaler le 1 de dec bits(celui de base est sur 16 bitys)
    masque & 0b11111111 #étape 2 : couper les bits en trop

    # EXEMPLE A TESTER : pour dec = 4, 0b1111111100000000 >> dec donne masque = 0b11110000 ou equivalent en entier

    return n & masque  # opérateur bitwise qui compare la valeur binaire de n et masque(deja binaire) et renvoi la partie ou les deux morceaux binaires 's'overlappent'

def decalage(n,dec):
    """
    param : un entier entre 0 et 255 , dec : intensité du decalage(par defaut 4)
    out : un entier entre 0 et 255 ; dont les bits de poids forts ont été décalés vers les bits de poids faible
    """
    return n >> dec 

def cache_image(im1_path,im2_path,bits_forts):
    """
    cache une image(im2) dans une autre image(im1) à l'aide de stéganogtraphie
    bits_forts : repartition des bits de poids forts de l'image 1 apres reduction
    """
    im1 = Image.open(im1_path).convert('RGB').resize((500,500))
    im2 = Image.open(im2_path).convert('RGB').resize((500,500))
    im_final = Image.new('RGB',(im1.width,im1.height))
    print(im1.size)
    print(im2.size)

    for x in range(im1.width):
        for y in range(im1.height):
            r,v,b = im1.getpixel((x,y))
            r,v,b = masque_faibles(r,bits_forts),masque_faibles(v,bits_forts),masque_faibles(b,bits_forts) #onn effectue unn masque de bits faibles sur l'image 1

            # on ne garde que les bits de poids forts des composantes RGB de l'image 1
            r2,v2,b2 = im2.getpixel((x,y))
            r2,v2,b2 = decalage(r2,bits_forts),decalage(v2,bits_forts),decalage(b2,bits_forts)
            # on fait passer les bits de poids fort des composantes RGB de l'image 2 en poids faible 
            im_final.putpixel((x,y),(r+r2,v+v2,b+b2))
            # on assembles les deux enntiers :
                # l'un étant codé sur 4 bits en poids fort (0 < n < 2^8-2^4)
                # l'autre étant codé sur 4 bits en poids faible(0 < n < 2^5-1)
                # avec ca o ne risque pas de dépasser la limite de 255
                # par contre on a une erreur de 32 maximale pour chaque composante
    im_final.save('images/fusion.png')
    im_final.show()

if __name__ == '__main__':
    im1 = Image.open('images/6.png').convert('RGB').resize((500,500))
    im2 = Image.open('images/9.jpeg').convert('RGB').resize((500,500))
    cache_image(im1,im2,1)
