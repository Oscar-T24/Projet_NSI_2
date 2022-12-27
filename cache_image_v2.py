from PIL import Image
# POUR CONVERTIR DES DECIMAUX EN BINAIRE ET VICE VERSA ON PEUX SIMPLEMENT UTILISER int() et bin()

im1 = Image.open('images/8.jpg').convert('RGB')
im2 = Image.open('images/7.jpg').convert('RGB')



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
            pixel1 = [bin(r)[:7],bin(v)[:7],bin(b)[:7]] # on garde les 5 premiers bits de poids fort du pixel 1
            #pixel1 = [pixel1[i]+(6-len(pixel1[i]))*'0' for i in range(3)] # on complete les 0 manquants
            pixel2 = [bin(r2)[:5],bin(v2)[:5],bin(b2)[:5]] # o garde les 3 premiers bits de poids fort du pixel 2
            #pixel2 = [pixel2[i]+(6-len(pixel2[i]))*'0' for i in range(3)] # on complete les 0 manquants
            pixel_final = [int(pixel1[i]+pixel2[i][2:],2) for i in range(3)] # on assemble les 5 premiers bits du pixel 1 avec les 3 premier bits du pixel 2          # option if pixel1[i] != '' and pixel2[i] != ''
            #try :
            im_final.putpixel((x,y),tuple(pixel_final))
            #except TypeError:
                #pass
    im_final.show()
        
cache_image(im1,im2)
''
