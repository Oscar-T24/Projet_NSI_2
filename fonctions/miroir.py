from PIL import Image
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

def miroir(image):
    '''
    image --> image
    renvoie une image retournée horizontalement
    '''
    # On récupère les pixels de l'image et on inverse l'image horizontalement
    pixels = [[image.getpixel((x, y)) for x in range(image.width)] for y in range(image.height)]
    pixels = [ligne[::-1] for ligne in pixels]
    image2 = Image.new('RGB', (image.width, image.height)) # On crée une image vide
    image2.putdata([pixel for ligne in pixels for pixel in ligne]) # On met les pixels dans l'image
    image2.save('images/miroir.png') # On sauvegarde l'image
    image2.show() # On affiche l'image

'''
# On appelle la fonction
image = Image.open('images/6.png').convert('RGB')
miroir('images/6.png')
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
    reveler = Button(menu1,text = 'effectuer un filtre mirroir',command = lambda:miroir(Image.open('images/'+clicked.get())))
    reveler.grid(row = 2, column = 0, pady = 5)
    comfirmer = Button(menu1, text = 'fermer cette fenetre',command = lambda:menu1.quit())
    comfirmer.grid(row = 4, column = 0, pady = 5)
    #entree = Entry(menu1, textvariable = passw_var, font = ('calibre',10,'normal'))
    #ntree.grid(row = 5,column = 0,pady = 5)
 
    menu1.mainloop() # executer le premier menu 

    return 

choisir_image()