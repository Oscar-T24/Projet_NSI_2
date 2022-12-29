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

im1 = Image.open('images/4.jpg').convert('RGB').resize((500,500))
im2 = Image.open('images/3.jpg').convert('RGB').resize((500,500))
'''
if im1.height > im2.height or im1.width > im2.width:
    im_final = Image.new('RGB',(im2.width,im2.height))
    im1.resize((im2.width,im2.height))
else :
    im_final = Image.new('RGB',(im1.width,im1.height))
    im2.resize((im1.width,im1.height))
'''
im_final = Image.new('RGB',(im1.width,im1.height))
print(im1.size)
print(im2.size)

for x in range(im1.width):
    for y in range(im1.height):
        r,v,b = im1.getpixel((x,y))
        r,v,b = masque_faibles(r),masque_faibles(v),masque_faibles(b)

        # on ne garde que les bits de poids forts des composantes RGB de l'image 1
        r2,v2,b2 = im2.getpixel((x,y))
        r2,v2,b2 = decalage(r2),decalage(v2),decalage(b2)
        # on fait passer les bits de poids fort des composantes RGB de l'image 2 en poids faible 
        im_final.putpixel((x,y),(r+r2,v+v2,b+b2))
        # on assembles les deux enntiers :
            # l'un étant codé sur 4 bits en poids fort (0 < n < 2^8-2^4)
            # l'autre étant codé sur 4 bits en poids faible(0 < n < 2^5-1)
            # avec ca o ne risque pas de dépasser la limite de 255
            # par contre on a une erreur de 32 maximale pour chaque composante
im_final.save('images/fusion.png')
im_final.show()

