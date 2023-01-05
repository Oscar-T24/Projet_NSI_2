from PIL import Image
# CE CODE EST UN PEU FOIREU
image = Image.open('images/8+7.png').convert('RGB')

def retrouve_image(image):
    '''
    prend en argument une image fusionnnée selon le script cache_image
    et renvoi la premiere image recomposée (a quelques erreur pres)
    '''

    image_final = Image.new('RGB',(image.size))
    for x in range(image.width):
        for y in range(image.height):
            #onn doit récupérer les 5 bits de poids fort et faire l'inverse des 3 derniers
            r, v, b = image.getpixel((x,y))
            pixel = [bin(r),bin(v),bin(b)] #on reprend nos pixels de 3 octets
            
            bits = ['1' if i2 == '0' else '0' for i in pixel for i2 in i[7:]] # oninverse les 3 derniers bits
            bits = [''.join(bits[i:i+3]) for i in range(0,len(bits)-2,3)]
            if len(bits) < 3:
                for i in range(3-len(bits)):
                    bits.append('0')

            print(len(bits), len(pixel))
            pixel = [int(pixel[i]+bits[i],2) for i in range(len(pixel))] # on reconverti tout en decimal

            image_final.putpixel((x,y),tuple(pixel))

    image_final.show()


retrouve_image(image)