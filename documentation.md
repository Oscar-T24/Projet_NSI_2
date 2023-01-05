https://towardsdatascience.com/steganography-hiding-an-image-inside-another-77ca66b2acb1

https://realpython.com/lessons/binary-numbers/


```
from PIL import Image

im = Image.open('images/fusion.png').convert('RGB') # l'image fusionnée
im_ini1 = Image.new('RGB',im.size) # on est contraint d'utiliser la taille de l'image fusionnée
im_ini2 = Image.new('RGB',im.size)

def decalage(n,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du decalage(par defaut 4)
    out : un entier entre 0 et 255 ; dont les bits de poids faibles ont été décalés vers les bits de poids fort
    """
    # comme on fait le processus inverse, on utilise le bitwise das l'autre sens
    return n << dec

def masque(n,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage(par defaut 4)
    out : un entier entre 0 et 255 ; sans bits de poids faibles
    """
    return n & 0b11110000  # opérateur bitwise qui compare la valeur binaire de n et masque(deja binaire) et renvoi la partie ou les deux morceaux binaires 's'overlappent'


for x in range(im.width):
    for y in range(im.height):
        r,v,b = im.getpixel((x,y))
        r1,v1,b1 = masque(r),masque(v),masque(b)
        r2,v2,b2 = masque(decalage(r)),masque(decalage(r)),masque(decalage(r))
        im_ini1.putpixel((x,y),(r1,v1,b1))
        im_ini2.putpixel((x,y),(r2,v2,b2))

im_ini1.show()
im_ini2.show()
```