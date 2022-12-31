from PIL import Image

def stegano(name_img , msg):

    im = Image.open(name_img)
    # on récupère les dimensions de l'image
    w , h = im.size
    # on sépare l'image en trois : rouge, vert et bleu (+transparence)
    rouge,g,b,t= im.split()
    # on transforme la partie rouge en liste
    rouge = list( rouge.getdata() )
    # on calcule la longueur de la chaîne et on la transforme en binaire
    longueur = len(msg)
    v = bin( len(msg) )[2:].rjust(8,"0")
    # on transforme la chaîne en une liste de 0 et de 1 
    ascii = [ bin(ord(x))[2:].rjust(8,"0") for x in msg ]
    # transformation de la liste en chaîne
    binaire_ascii = ''.join(ascii)
    # on code la longueur de la liste dans les 8 premiers pixels rouges

    for j in range(8):
        rouge[j] = 2 * int( rouge[j] // 2 ) + int( v[j] )

    # on code la chaîne dans les pixels suivants
    for i in range(8*longueur):
        rouge[i+8] = 2 * int( rouge[i+8] // 2 ) + int( binaire_ascii[i] )
        
    # on recrée l'image rouge 
    nrouge = Image.new("L",(16*w,16*h))
    nrouge = Image.new("L",(w,h))
    nrouge.putdata(rouge)
    # fusion des trois nouvelles images
    imgnew = Image.merge('RGB',(nrouge,g,b))
    '''new_name_img = "couv_" + name_img'''
    imgnew.save('images/texte_cache.png')

stegano("images/10.png" , "MDR !")

def get_msg(name_couv):
    im = Image.open(name_couv)
    r , g , b = im.split()
    r = list( r.getdata() )
    
    # lecture de la longueur de la chaine
    p = [ str(x%2) for x in r[0:8] ]
    q = "".join(p)
    q = int(q,2)
    
    # lecture du message
    n = [ str(x%2) for x in r[8:8*(q+1)] ]
    b = "".join(n)
    message = ""
    for k in range(0,q):
        l = b[8*k:8*k+8]
        message += chr(int(l,2))
        
    return message

print(get_msg('images/texte_cache.png'))