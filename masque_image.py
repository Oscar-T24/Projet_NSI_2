from PIL import Image
n = 159                     # entier entre 0 et 255
masque = 0b11110000         # entier en binaire, 8 bits

m = n & masque


def masque_faibles(n,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage(par defaut 4)
    out : un entier entre 0 et 255 ; sans bits de poids faibles
    """
    return n & 0b11110000  # opérateur bitwise qui compare la valeur binaire de n et masque(deja binaire) et renvoi la partie ou les deux morceaux binaires 's'overlappent'

def decalage(n,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du decalage(par defaut 4)
    out : un entier entre 0 et 255 ; dont les bits de poids forts ont été décalés vers les bits de poids faible
    """
    return n >> dec 

im1 = Image.open('images/8.jpg').convert('RGB')
im2 = Image.open('images/7.jpg').convert('RGB')

im_final = Image.new('RGB',im1.size)
for x in range(im1.width):
    for y in range(im1.height):
        r,v,b = im1.getpixel((x,y))
        r,v,b = masque_faibles(r),masque_faibles(v),masque_faibles(b)
        # on ne garde que les bits de poids forts des composantes RGB de l'image 1
        r2,v2,b2 = im2.getpixel((x,y))
        r2,v2,b2 = decalage(r2),decalage(v2),decalage(b2)
        # on fait passer les bits de poids fort des composantes RGB de l'image 2 en poids faible 
        print(r+r2,v+v2,b+b2)
        pass
        im_final.putpixel((x,y),(r+r2,v+v2,b+b2))

im_final.show()

