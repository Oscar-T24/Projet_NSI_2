from revele_cache_texte import cache_texte, trouve_texte
from PIL import Image
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import time


def choisir_image():
    def cache():
          message=passw_var.get()
          cle=cletexte.get()
          if message != '':
            try:
              cache_texte(message, Image.open('images/'+clicked.get()),int(cle))    
            except ValueError:
               print('VEUILLEZ ENTRER UNE CLEDE DECHIFFRAGE : NE LAISSEZ PAS VIDE')
          else:
            raise Exception('VEUILLEZ ENTRER UN MESSAGE') from cache_texte()
    menu1 = Tk()
    menu1.geometry( "300x600" )
    passw_var=StringVar()
    cletexte=StringVar()

    def image(image):
        if image == 1: 
          label.config(text = clicked.get())
          try :
            initial = Image.open('images/'+clicked.get()).resize((170,170))
            test = ImageTk.PhotoImage(initial)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.place(x=60, y=300)
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
    reveler = Button(menu1,text = 'reveler un message',command = lambda:print(trouve_texte(Image.open('images/'+clicked.get()),int(cletexte.get()))))
    reveler.grid(row = 2, column = 0, pady = 5)
    cacher = Button(menu1,text = 'cacher du texte dans l"image selectionnnée',command = cache)
    cacher.grid(row = 3, column = 0, pady = 5)
    comfirmer = Button(menu1, text = 'fermer et commencer',command = lambda:menu1.quit())
    comfirmer.grid(row = 4, column = 0, pady = 5)
    entree = Entry(menu1, textvariable = passw_var, font = ('calibre',10,'normal'))
    entree.grid(row = 5,column = 0,pady = 5)
    label3 = Label(menu1, text = "entrez votre message")
    label3.grid(row = 6,column = 0,pady = 0)
    entree2 = Entry(menu1, textvariable = cletexte, font = ('calibre',10,'normal'))
    entree2.grid(row = 7,column = 0,pady = 5)
    label2 = Label(menu1, text = "entrer la clé de (dé)chiffrage")
    label2.grid(row = 8,column = 0,pady = 0)
 
    menu1.mainloop() # executer le premier menu 

    return 'images/'+clicked.get(),entree.get()

print(choisir_image())