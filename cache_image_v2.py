from PIL import Image
# POUR CONVERTIR DES DECIMAUX EN BINAIRE ET VICE VERSA ON PEUX SIMPLEMENT UTILISER int() et bin()

im1 = Image.open('images/8.jpg').convert('RGB')
im2 = Image.open('images/9.jpeg').convert('RGB')



def cache_image(im1,im2):
    '''
    img,img --> img
    cache l'image 2 dans l'image 1 par scetanographie
    '''
    if im2.size[0] > im1.size[0] or im2.size[1] > im1.size[1]:
        raise ValueError('les images sont pas à la meme taille!')
    '''
    if im1.size > im2.size :
        im_final = Image.new('RGB',(im2.width,im2.height))
        im1.resize((im2.width,im2.height))
    else :
        im_final = Image.new('RGB',(im1.width,im1.height))
        im2.resize((im1.width,im1.height))
    '''
    im_final = Image.new('RGB',(im1.width,im1.height))
    # pour rappel, chaque composante d'un pixel est codée sur 8 bits : de 0 à 255 variantes d'une couleur
    for x in range(im1.width):
        for y in range(im1.height):
            r, v, b = im1.getpixel((x,y))
            r2,v2,b2 = im2.getpixel((x,y))

    # NOTE : au format binaire , les bits de poids faible sont à droite tandis que les bits de poids forts sont à gauche 

            pixel1 = [bin(r)[:6],bin(v)[:6],bin(b)[:6]] # on garde les 4 premiers bits de poids fort du pixel 1``
            #pixel1 = [pixel1[i]+(6-len(pixel1[i]))*'0' for i in range(3)] # on complete les 0 manquants
            pixel2 = [bin(r2)[:6],bin(v2)[:6],bin(b2)[:6]] # o garde les 4 premiers bits de poids fort du pixel 2
            #pixel2 = [pixel2[i]+(6-len(pixel2[i]))*'0' for i in range(3)] # on complete les 0 manquants
            pixel_final = [int(pixel2[i]+pixel1[i][2:],2) for i in range(3)] # on assemble les 4 premiers bits du pixel 1 avec les 4 premier bits du pixel 2         

            im_final.putpixel((x,y),tuple(pixel_final))
            #except TypeError:
                #pass
    im_final.save('images/8+7.png')
    im_final.show()
        
cache_image(im1,im2)

class Steganography : 
    def self():
        pass

