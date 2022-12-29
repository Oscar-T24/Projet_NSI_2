# ce code ferait notre fonction 'de_notre_chioix'
# cela consisterait à faire un algorithme qui puisse coder un message dans uen image en utilisant l'encodage ASCII
# en cas de manque de place on pourrai ajouter une compression en  RUN LENGTH ENCODING (RLE) qui serait u second 'filtre'

def cache_texte(message,image):
    binaire =  [format(ord(x), '#010b')[2:] for x in message]
    binaire = [[e[:len(e)//2]]+[e[len(e)//2:]] for e in binaire]
    binaire = [element for sublist in binaire for element in sublist]
    indice = 0
    for x in image.width:
        for y in image.height:
            if indice < len(binaire): # si o a dépassé l'indice des octets à écrire et qu'il nous reste des pixels, arreter le processus d'ecriture
                indice += 1
            else:
                break
            r,v,b = image.getpixel((x,y))
            r,v,b = masque_faibles(r), masque_faibles(v), masque_faibles(b)
            image_final.putpixel((x,y),(r+))

cache_texte(input('entrer un message ASCII à cacher'),'t')



def masque_faibles(n,dec=4):
    """
    param : un entier entre 0 et 255 , dec : intensité du masquage(par defaut 4)
    out : un entier entre 0 et 255 ; sans bits de poids faibles
    """
    return n & 0b11110000 


def compression_rle(tableau):
    '''
    parcours une matrice d'octets representant un caractere chacun
    '''
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
