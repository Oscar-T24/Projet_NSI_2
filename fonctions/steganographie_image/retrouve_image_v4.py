from PIL import Image
from cache_image_V4 import masque_faibles


def decalage(n,dec):
    """
    param : un entier entre 0 et 255 , dec : intensité du decalage(par defaut 4)
    out : un entier entre 0 et 255 ; dont les bits de poids faibles ont été décalés vers les bits de poids fort
    """
    # comme on fait le processus inverse, on utilise le bitwise das l'autre sens
    return n << dec

def retrouve_image(im_path,bits_forts):
    image = Image.open(im_path).convert('RGB') # l'image fusionnée
    im_ini1 = Image.new('RGB',image.size) 
    im_ini2 = Image.new('RGB',image.size)

    for x in range(image.width):
        for y in range(image.height):
            r,v,b = image.getpixel((x,y))
            r1,v1,b1 = masque_faibles(r,bits_forts),masque_faibles(v,bits_forts),masque_faibles(b,bits_forts)
            r2,v2,b2 = decalage(r,bits_forts)&0b11111111,decalage(v,bits_forts)&0b11111111,decalage(b,bits_forts)&0b11111111
            
            # on utilise & 0b11111111 pour garder que 8 bits car en decalant on multiplie par 2 / on ajoute des zeros à gauche ce qui fait que l'image 2 dépasse 255

            im_ini1.putpixel((x,y),(r1,v1,b1))
            im_ini2.putpixel((x,y),(r2,v2,b2))

    im_ini1.show()
    im_ini2.show()
    
if __name__ == '__main__':
    pass