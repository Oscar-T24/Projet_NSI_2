from PIL import Image, ImageFilter
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

# NE FONCTIONERA PAS AVEC UNE IMAGE JPEG
# CREE UNE IMAGE FLOUTÉE E FAISANT LA MOYENNE DES PIXELKS ENVIRONNNANTS

# ce qu'il faudrait faire : utilise une matrice (ou array pour stocker les composantes RGB de chaque 'bloc' de pixels environnants)


def flou(image,rayon): 
    '''
    pixels = nombre de pixels en longeur et largeur
    img(png), int(pixels) -> img(png, floutée)
    fait pour chaque pixel la moyene du pixel et de celle des 8 pixels avoisinants
    '''
    #taille_ini = (image.width,image.height)
    rgb_im = image.convert('RGB') # on coverti en RGB pour maipuler les composantes vertes, rouges et blueus
    rgb_im_final = Image.new('RGB',image.size) # on crée une image qui sera modifiée ; l'autre initiale est utilisée comme guide
    
    for x in range(rayon,image.width-(rayon+1)):
        for y in range(rayon,image.height-(rayon+1)):

            # ------------------------PARTIE PARCOURS --------------------------------------------------

            liste_rgb = [0,0,0]        
            comptage = 0
            for voisin_x in range(x-rayon,x+rayon,rayon//2): # ON UTILISE UN INCNREMENT DE L     RAYON POUR NE PAS REECRIRE PLUSIEURS FOIS SUR LES MEMES PIXELS
                for voisin_y in range(y-rayon,y+rayon,rayon//2):
                    r, g, b = rgb_im.getpixel((voisin_x,voisin_y))
                    liste_rgb[0] += r
                    liste_rgb[1] += g
                    liste_rgb[2] += b
                    comptage += 1

            # on obtient une liste de 9 élements(chaque element ayant une composante RGB)


            # ------------------------PARTIE MOYENNE DE CHAQUE COMPOSANNT ----------------------------
            moyenne = [round((liste_rgb[i])/comptage) for i in range(3)]
            # ----------------------------------------------------------------------------------------

            # -----------------------------------ECRITURE PIXELS--------------------------------------
            rgb_im_final.putpixel((x, y), (moyenne[0],moyenne[1],moyenne[2]))
            # ----------------------------------------------------------------------------------------
    rgb_im_final.show()
    rgb_im.show()

'''
# CETTE FONCTION ABOUTIE A FAIRE LE FILTRE BOXBLUR DE LA LIBRAIRIE PIL

# Opens a image in RGB mode
im = Image.open('images/9.png')

# Blurring the image
im1 = im.filter(ImageFilter.BoxBlur(12))

# Shows the image in image viewer
im1.show()
'''
def choisir_image():   
    menu1 = Tk()
    menu1.geometry( "200x400" )
    passw_var=StringVar()
    cletexte=StringVar()

    def image(image):
        if image == 1: 
          label.config(text = clicked.get())
          try :
            image1 = Image.open('images/'+clicked.get()).resize((170,170))
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.place(x=5, y=200)
            #time.sleep(5)
            #label1.destroy()

          except FileNotFoundError:
            print('fichier inexistant')
        
    options = os.listdir('images')
    options = [e for e in options if '.png' or '.jpg' or '.jpeg' in e and 'fusion.png' not in e]
    clicked = StringVar()
    clicked.set( "choisissez une photo no 1" )
    drop = OptionMenu( menu1 , clicked , *options )
    drop.grid(row = 0, column = 0, pady = 5)
    label = Label(menu1 , text = " " )
    label2 = Label(menu1 , text = " " )
    button = Button( menu1 , text = "précharger image 1" ,command = lambda:image(1))
    button.grid(row = 1, column = 0, pady = 5)
    reveler = Button(menu1,text = 'effectuer un filtre flou',command = lambda:flou(Image.open('images/'+clicked.get()),int(cletexte.get())))
    reveler.grid(row = 2, column = 0, pady = 5)
    comfirmer = Button(menu1, text = 'fermer cette fenetre',command = lambda:menu1.quit())
    comfirmer.grid(row = 4, column = 0, pady = 5)
    entree2 = Entry(menu1, textvariable = cletexte, font = ('calibre',10,'normal'))
    entree2.grid(row = 5,column = 0,pady = 0)
    label2 = Label(menu1, text = "entrer le rayon de floutage")
    label2.grid(row = 6,column = 0,pady = 0)
 
    menu1.mainloop() # executer le premier menu 

    return 

choisir_image()