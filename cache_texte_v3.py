'''
CETTE SECODE VERSION ENCODERA UNBIQUEMENT 1 BIT PAR COMPOSANTE (car probleme sur la premiere version)
'''
'''
FONCTION INTEGRÉS UTILES : 
ord(x) : caractere ASCII --> entier entre 0-255
chr(x) : binnaire (obxxxxxxxx) --> caractere ASCII
.rjust(8,'0') : rajoute des 0 pour avoir 8 bits (un octet)

'''
from PIL import Image

def masque(n,mode,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage(par defaut 4)
    out : un entier entre 0 et 255 ; sans bits de poids faibles ou foirt selon le masque
    """
    match mode:
        case 'faible':
            return n & 0b00000001
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
    binaire = [format(ord(x), '#010b') for x in message] # binaire : liste d'octets codant chacun un caratère (au format 0bxxxxxxxx en string)
    binaire = ''.join([digit for octet in binaire for digit in octet[2:]]) # binaire : liste de digits les uns derriere les autres sans 0b
    indice = 0 
    '''
    for i in range(len(binaire)-2):
        print(binaire[i],binaire[i+1],binaire[i+2])
    '''
    print(binaire)
    for x in range(image.width):
        for y in range(image.height):
            r,v,b = image.getpixel((x,y))
            r = masque(r,'fort')
             #enleve le bit de poids le plus faible. On pourrai faire plus simplement en arrondissant la composante au nombre pair le plus proche(ce qui reviendrai à enlever le premier bit 1)
            image_final.putpixel((x,y),(r |int(binaire[indice]),v,b))
            #image_final.putpixel((x,y),(r,v,b))
            if indice < len(binaire)-1 : # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                # le -3 est la car à chaque fois on ecrit de indice à indice+3 sur les composantes RGB
                indice +=1
            else:
                break
            
    image_final.show()
    '''# ---------------
    liste_rgb = []
    for x in range(8):
        for y in range(8):
            rouge,vert,bleu = image_final.getpixel((x,y))
            liste_rgb.append([rouge,vert,bleu])
    print(liste_rgb)
    '''# ---------------
    image_final.save('images/messager.png', format = 'PNG')
    print('message de longueur', len(binaire))
    print(binaire)

im1 = Image.open('images/logoIsnIrem.png').convert('RGB')
cache_texte(input('entrer un message ASCII à cacher'),im1)


def trouve_texte(image, longueur):
    message = ''
    indice = 0
    binaire = ''
    for x in range(image.width):
        for y in range(image.height):
            r,v,b = image.getpixel((x,y))
            r = masque(r,'faible')
            binaire+=str(r)
            if indice < longueur-1: # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                indice += 1
            else:
                break
    binaire = binaire[:longueur]
    print(binaire)
    octets = [chr(int('0b'+binaire[i:i+9],2)) for i in range(longueur)]
    #octets = ''.join([chr(int('0b'+binaire[i:i+9],2)) for i in range(longueur)]) #ecriture des octets
    print(octets)
    return message
im_a_decoder = Image.open('images/messager.png').convert('RGB')
trouve_texte(im_a_decoder,int(input('longueur du message')))
   

# -------------
'''
im_a_decoder = Image.open('images/messager.png').convert('RGB')
liste_rgb = []
for x in range(8):
    for y in range(8):
        rouge,vert,bleu = im_a_decoder.getpixel((x,y))
        liste_rgb.append([rouge,vert,bleu])
print(liste_rgb)
'''
# -------------