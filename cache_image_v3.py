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
            pixel1 = []
            pixel2 = []
            r, v, b = im1.getpixel((x,y))
            r2,v2,b2 = im2.getpixel((x,y))
            # ASSEMBLAGE DES 4 bits de poids fort de chaque pixel
            
            pixel1 = [bin(r),bin(v),bin(b)]
            pixel2 = [bin(r2),bin(v2),bin(b2)]
            pixel_final = [0,0,0]
            for i in range(3):
                pixel_final[i] = int(pixel1[i][:6]+pixel2[i][2:6],base=0)
                #print('fusion de ' ,pixel1[i][:6], ' . et ',pixel2[i][2:6],'pour donner',pixel_final[i] )

            im_final.putpixel((x,y),tuple(pixel_final))



    #im_final.save('images/8+7.png')
    im_final.show()
        
cache_image(im1,im2)
''


