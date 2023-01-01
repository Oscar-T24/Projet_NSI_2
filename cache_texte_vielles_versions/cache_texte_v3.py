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
        print(binaire[i],binire[i+1],binaire[i+2])
    '''
    print('message codé en bits: ',binaire)
    for x in range(image.width):
        for y in range(image.height):
            #image_final.putpixel((x,y),(r,v,b))
            if indice < len(binaire): # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                r,v,b = image.getpixel((x,y))
                r = masque(r,'fort')
                    #enleve le bit de poids le plus faible. On pourrai faire plus simplement en arrondissant la composante au nombre pair le plus proche(ce qui reviendrai à enlever le premier bit 1)
                image_final.putpixel((x,y),(r |int(binaire[indice]),v,b))
            indice +=1
            if indice > len(binaire): # on écrit un drapeau pour marquer la fin du message (celui ci est purement arbitraire)
                image_final.putpixel((x,y),(255 & 0b01010101,255 & 0b00001111,255 & 0b00111100))
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

im1 = Image.open('images/6.png').convert('RGB')
#cache_texte(input('entrer un message ASCII à cacher'),im1)


def trouve_texte(image):
    message = ''
    indice = 0
    binaire = ''
    for x in range(image.width):
        for y in range(image.height):
            r,v,b = image.getpixel((x,y))
            if r == 85 and v == 15 and b == 60: # c'est un flag random mais ya vrmt peu de chance que ca tombre dessus
                longueur = len(binaire)
                break
            else:
                r = masque(r,'faible')
            binaire+=str(r)
            '''
            if indice < longueur-1: # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                indice += 1
            else:
            '''
    binaire = binaire[:longueur]
    
    print('message codé en bits retrouvé : ',binaire)
    octets = ''.join([chr(int('0b'+binaire[i+1:i+8],2)) for i in range(0,longueur,8)]) #ecriture des octets
    print(octets)
    return message
im_a_decoder = Image.open('images/messager.png').convert('RGB')
trouve_texte(im_a_decoder)
   

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