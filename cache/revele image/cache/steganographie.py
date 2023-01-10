from revele_cache_texte import cache_texte, trouve_texte
from PIL import Image
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import time


def choisir_image():
    def cache():
          bits=passw_var.get()
          cache_texte(bits, Image.open('images/'+clicked.get()))     
    menu1 = Tk()
    menu1.geometry( "300x600" )
    passw_var=StringVar()

    def image(image):
        if image == 1: 
          label.config(text = clicked.get())
          try :
            image1 = Image.open('images/'+clicked.get()).resize((170,170))
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(image=test)
            label1.image = test
            label1.place(x=75, y=260)
            #time.sleep(5)
            #label1.destroy()

          except FileNotFoundError:
            print('fichier inexistant')
        
    options = os.listdir('images')
    options = [e for e in options if '.png' or '.jpg' or '.jpeg' in e and 'fusion.png' not in e]
    clicked = StringVar()
    clicked.set( "choisissez une photo no 1" )
    drop = OptionMenu( menu1 , clicked , *options )
    drop.pack()

    # instatiation des boutons à partir de la classe Bouton
    label = Label(menu1 , text = " " )
    label.pack()
    label2 = Label(menu1 , text = " " )
    label2.pack()
    button = Button( menu1 , text = "précharger image 1" ,command = lambda:image(1)).pack() # .grid(row=1,column=0)
    reveler = Button(menu1,text = 'reveler un message',command = lambda:trouve_texte(Image.open('images/'+clicked.get()))).pack()
    cacher = Button(menu1,text = 'cacher du texte dans l"image selectionnnée',command = cache).pack()
    comfirmer = Button(menu1, text = 'fermer et commencer',command = lambda:menu1.quit()).pack()
    entree = Entry(menu1, textvariable = passw_var, font = ('calibre',10,'normal')).pack()

    menu1.mainloop() # executer le premier menu 

    return 'images/'+clicked.get(),entree.get()

print(choisir_image())