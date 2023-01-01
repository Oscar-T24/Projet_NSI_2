# ce code ferait notre fonction 'de_notre_chioix'
# cela consisterait à faire un algorithme qui puisse coder un message dans uen image en utilisant l'encodage ASCII
# en cas de manque de place on pourrai ajouter une compression en  RUN LENGTH ENCODING (RLE) qui serait u second 'filtre'
from PIL import Image

def masque(n,mode):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage(par defaut 4)
    out : un entier entre 0 et 255 ; sans bits de poids faibles ou foirt selon le masque
    """
    match mode:
        case 'faible':
            return n & 0b00001111
        case 'fort':
            return n & 0b11110000 

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
    image_final = image.copy() # soit on crée unne ouvelle image, soit on copie l'autrre ca reste à décider
    binaire = [format(ord(x), '#010b') for x in message] 
    binaire = [[decalage(masque(int(e,2),'fort'),'droite')]+[masque(int(e,2),'faible')] for e in binaire]
    binaire = [element for sublist in binaire for element in sublist]
    print(binaire)
    indice = 0
    liste_rgb1 = []
    for x in range(image.width):
        for y in range(image.height):
            if indice < len(message)-2: # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                indice += 1
            else:
                break
            '''
            # ---------------- UNIQUEMET POUR DEBOGAGE
            rouge,vert,bleu = image_final.getpixel((x,y))
            liste_rgb1.append([rouge,vert,bleu])
            # -----------------
            '''
            r,v,b = image.getpixel((x,y))
            r,v = masque(r,'fort'), masque(v,'fort')
            image_final.putpixel((x,y),(r+binaire[indice],v+binaire[indice+1],b))
    image_final.show()
    '''# -------------------- uniquempent debogage
    liste_rgb2 = []
    for x in range(2):
        for y in range(2):
            rouge,vert,bleu = image_final.getpixel((x,y))
            liste_rgb2.append([rouge,vert,bleu])

    '''# --------------------
    image_final.save('images/messager.png', format = 'PNG')
    
    print('message de longueur', len(message)) # ATTENTION LA LONGUEUR DU MESSAGE EST DEUX FOIS MOINS LONGUE DE CELLE DES COMPOSATES À PARCOURIR
    '''
    print('sequennce 1 de pixels RGB', liste_rgb1)
    print('\n sequence ouvelle (2) de pixels apres ecriture', liste_rgb2)
    '''
im1 = Image.open('images/logoIsnIrem.png').convert('RGB')
cache_texte(input('entrer un message ASCII à cacher'),im1)

def trouve_texte(image, longueur):
    message = ''
    indice = 0
    binaire = []
    for x in range(image.width):
        for y in range(image.height):
            if indice < longueur-2: # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                indice += 1
            else:
                break
            r,v,b = image.getpixel((x,y))
            r,v = masque(r,'faible'), masque(v,'faible')
            #r,v,b = bin(decalage(r,'gauche')),bin(v),bin(decalage(b,'gauche'))
            binaire.append(r)
            binaire.append(v)
    for i in range(len(binaire)-1):
        message+=(chr(decalage(binaire[i],'gauche')+binaire[i+1]))
        

    return message
im_a_decoder = Image.open('images/messager.png').convert('RGB')
print(trouve_texte(im_a_decoder,int(input('longueur du message'))))
    
'''
def compression_rle(tableau):
    """
    parcours une matrice d'octets representant un caractere chacun
    """
    tableau_rle = []
    for i in range(len(tableau)): # rangée par rangée
        compte = 1
        m = [] # créeation d'une variable pour une rangée 
        for i2 in range(1,len(tableau[i])):   

            if tableau[i][i2-1] == 1 and i2 == 1:
                m.append(0)
            if tableau[i][i2-1] == tableau[i][i2]:
                compte += 1           
            else:
                m.append(compte)
                compte = 1    
        m.append(compte)   
        tableau_rle.append(m)
    return tableau_rle
compte = 0
binaire = '01100010 01101111 01101110 01101010 01101001 01101111 01110101 01110010 00100000 01101010 01100101 00100000 01101101 00100111 01100001 01110000 01100101 01101100 01101100 01100101 00100000 01101111 01110011 01100011 01100001 01110010 00100000 01101010 00100111 01100001 01101001 00100000 00110001 00110111 00100000 01100001 01101110 01110011 00100000 01100101 01110100 00100000 01101010 01100101 00100000 01101101 01100001 01101110 01100111 01100101 00100000 01100010 01100101 01100001 01110101 01100011 01101111 01110101 01110000'.split(' ')
for e in binaire:
    for e2 in binaire:
        e2 = e2 + ' '
        compte += 1
print('il y a ',compte, 'digits')
print(binaire)
tableau = compression_rle(binaire)
compte = 0
for e in tableau:
    for e2 in e:
        compte += 1
print('il y a ',compte, 'chiffres')
print(tableau)

# si la rangée commence par un 1, il faut mettre un 0 pour indiquer la difference

# on obtient unn tableau donnant l'encodage binaire ASCII encodé en RLE

# FORMAT D'ENCODAGE  : on écrit une séquence(1 caractere autrement dit) séparé d'un espace de 0000 ; onn prend 4 bits à chaque fois
'''