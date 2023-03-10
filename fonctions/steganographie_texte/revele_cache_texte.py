'''
CETTE QUATRIEME VERSION ENCODERA 2 BIT PAR COMPOSANTE SUR ROUGE ET VERT 
A RAJOUTER : OPTIONN DE CRYPTAGE ET DECRYPTAGE À LA MODE CESAR : https://fraoustin.fr/old/20111222_1.html
'''
'''
FONCTION INTEGRÉS UTILES : 
ord(x) : caractere ASCII --> entier entre 0-255
chr(x) : binnaire (obxxxxxxxx) --> caractere ASCII
.rjust(8,'0') : rajoute des 0 pour avoir 8 bits (un octet)
'''
from PIL import Image
from methode_Cesar import encode_words, decode_words
import time

def masque(n,mode,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage(par defaut 4)
    out : un entier entre 0 et 255 ; sans bits de poids faibles ou foirt selon le masque
    """
    match mode:
        case 'faible':
            return n & 0b00000011
        case 'fort':
            return n & 0b11111100

'''
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
'''
# -------------------- CACHE TEXTE -------------------------------------------
def cache_texte(message,image,cle):
    """
    param : un message en caractere ASCII , et une image dans laquelle encoder le message
    out : une image codée avec un texte
    """
    image_final = image.copy() #copier l'image permet d'evioter à parcourir à nouveau l'image enj entier mais juste la partie dans laquelle on code le message
    longueur = bin(len(message))[:2]
    message = encode_words(message,cle)
    binaire = [format(ord(x), '#010b') for x in message] # binaire : liste d'octets codant chacun un caratère (au format 0bxxxxxxxx en string)
    binaire = ''.join([digit for octet in binaire for digit in octet[2:]]) # binaire : liste de digits les uns derriere les autres sans 0b
    indice = 0 

    #print('message codé en bits: ',binaire)
    for x in range(image.width):
        for y in range(image.height):
            #image_final.putpixel((x,y),(r,v,b))
            if indice < len(binaire): # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                try :
                    r,v,b = image.getpixel((x,y))
                except ValueError:
                    r,v,b,t = image.getpixel((x,y)) # si l'image est au format PNG, ajouter une 4e composante, la transparence
                r,v,b = masque(r,'fort'),masque(v,'fort'),masque(b,'fort')
                    #enleve le bit de poids le plus faible. On pourrai faire plus simplement en arrondissant la composante au nombre pair le plus proche(ce qui reviendrai à enlever le premier bit 1)
                image_final.putpixel((x,y),(r  | int(binaire[indice:indice+1]),v |int(binaire[indice+1:indice+2]),b))
            indice +=2 #ON DECALE DE DEUX INDICES         
            if indice > len(binaire): # on écrit un drapeau pour marquer la fin du message : si une composante bleu possède un 1 en bit de poids faible, on arrete de lire le message(car on met un 0 partout autrement)
                image_final.putpixel((x,y),(r,v,b | 0b00000001))
                break     
    image1_size = image.size
    image2_size = image_final.size
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image,(0,0))
    new_image.paste(image_final,(image1_size[0],0))
    image_final.save("images/messager.png",format = "PNG")
    new_image.show()
    #print('message de longueur', len(binaire))
    #print(binaire)
# -------------------- TROUVE TEXTE -------------------------------------------
def trouve_texte(image,cle):
    """
    retrouve un texte caché dans une image
    out : le message caché
    """
    binaire = ''
    for x in range(image.width):
        for y in range(image.height):
            try :
                r,v,b = image.getpixel((x,y))
            except ValueError:
                r,v,b,t = image.getpixel((x,y))
            if b % 2 != 0: # si on a un 1 comme bit de poids faible, on arrete de lire les octets(= fin de message)
                longueur = len(binaire)
                break
            else:
                r,v = masque(r,'faible'),masque(v,'faible')
            binaire+=str(r)
            binaire+=str(v)
    try:
        binaire = binaire[:longueur]
    except UnboundLocalError :
        print('MESSAGE TROP LONG : LE MESSAGE DEPASSE DE L"IMAGE ET NE PEUT PAS ETRE LU')
    
    print('message co dé en bits retrouvé : ',binaire)
    octets = ''.join([chr(int('0b'+binaire[i+1:i+8],2)) for i in range(0,longueur,8)]) #ecriture des octets

    return decode_words(octets,cle)

'''
im1 = Image.open('images/11.png').convert('RGB')
cache_texte(input('entrer un message à cacher'),im1,4)
time.sleep(5)
im_a_decoder = Image.open('images/messager.png').convert('RGB')
print(trouve_texte(im_a_decoder,4))
'''
''' texte lorem ipsum pour tester ! 
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Vestibulum commodo fermentum massa at dignissim. Sed vel
  consectetur tellus. Praesent mattis aliquet orci, pulvina
  r vestibulum purus commodo vel. Proin pulvinar a libero ut 
  laoreet. Integer lorem massa, luctus eget felis at, congue 
  imperdiet augue. Vivamus erat velit, varius eu erat dapibus,
   ultricies feugiat velit. Donec commodo, ipsum eget feugiat sodales,
    orci arcu convallis massa, et placerat magna purus eget lorem. 
    Integer nec felis nunc. Vestibulum sed ipsum lacinia, feugiat sapien vitae,
     sodales mi. Etiam ac facilisis metus, sit amet tempor lacus. 
     Vivamus ullamcorper felis lectus, sed pulvinar lacus blandit non.
      Aenean tempor urna at ipsum imperdiet, vitae blandit leo maximus.
       Duis non ornare tortor. Nam in nulla ornare, 
       sollicitudin erat sit amet, mollis orci. Suspendisse fringilla 
       in eros vitae condimentum. Donec ut cursus purus.
       Nunc pretium ipsum vel mi ultrices, sit amet luctus erat pellentesque. 
       Curabitur consequat justo mi, a posuere lectus
'''