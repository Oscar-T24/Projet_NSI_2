from PIL import Image

def masque(n,mode,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage(par defaut 4)
    out : un entier entre 0 et 255 ; sans bits de poids faibles ou foirt selon le masque
    """
    match mode:
        case 'faible':
            return n & 0b00001111
        case 'fort':
            return n & 0b11111110 

def decalage(n,mode,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du decalage(par defaut 4)
    out : un entier entre 0 et 255 ; dont les bits de poids forts ont été décalés vers les bits de poids faible
    """
    match mode:
        case 'droite':
            return n >> dec 
        case 'gauche':
            return n << dec 

def cache_texte(message,image):
    image_final = image.copy()
    longueur = bin(len(message))[:2]
    binaire = [format(ord(x), '#010b') for x in message] 
    binaire = [digit for octet in binaire for digit in octet[2:]]
    binaire = ''.join(binaire)
    
    print(binaire)
    return
    for x in range(image.width):
        for y in range(image.height):
            if indice < len(message): # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                indice += 1
            else:
                break
            r,v,b = image.getpixel((x,y))
            r,v,b = masque(r,'fort'), masque(v,'fort'), masque(b,'fort') #enleve le bit de poids le plus faible
            image_final.putpixel((x,y),())
    image_final.show()
    image_final.save('images/messager.png', format = 'PNG')
    print('message de longueur', len(message))

im1 = Image.open('images/logoIsnIrem.png').convert('RGB')
cache_texte(input('entrer un message ASCII à cacher'),im1)

def trouve_texte(image, longueur):
    message = ''
    indice = 0
    binaire = []
    for x in range(image.width):
        for y in range(image.height):
            if indice < longueur-3: # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                indice += 1
            else:
                break
            r,v,b = image.getpixel((x,y))
            r,v,b = masque(r,'faible'), masque(v,'faible'), masque(b,'faible')
            #r,v,b = bin(decalage(r,'gauche')),bin(v),bin(decalage(b,'gauche'))
            binaire.append(r)
            binaire.append(v)
            binaire.append(b)

    print(binaire)

    return message
im_a_decoder = Image.open('images/messager.png').convert('RGB')
trouve_texte(im_a_decoder,int(input('longueur du message')))
   