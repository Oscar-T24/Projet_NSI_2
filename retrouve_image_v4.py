from PIL import Image
from cache_image_V4 import masque_faibles

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

for x in range(im.width):
    for y in range(im.height):
        r,v,b = im.getpixel((x,y))
        r1,v1,b1 = masque_faibles(r),masque_faibles(v),masque_faibles(b)
        r2,v2,b2 = decalage(r)&0b11111111,decalage(v)&0b11111111,decalage(b)&0b11111111
        
        # on utilise & 0b11111111 pour garder que 8 bits car en decalant on multiplie par 2 / on ajoute des zeros à gauche ce qui fait que l'image 2 dépasse 255

        im_ini1.putpixel((x,y),(r1,v1,b1))
        im_ini2.putpixel((x,y),(r2,v2,b2))

im_ini1.show()
im_ini2.show()