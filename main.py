
import sys
from PIL import Image
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import time


def menu_principal():
    def cache():
        pass
    def image(image):
        pass  
    menu1 = Tk()
    menu1.geometry( "300x600" )
    # instatiation des boutons à partir de la classe Bouton
    label = Label(menu1 , text = " " )
    label.pack()
    label2 = Label(menu1 , text = " " )
    label2.pack()
    bouton1 = Button(menu1,text = 'effectuer un effet de flou sur une image',command = lambda:os.system("python3 fonctions/flou.py")).pack()
    bouton3 = Button( menu1 , text = "effectuer l'effet mirroir sur une image" ,command = lambda:os.system("python3 fonctions/mirroir.py")).pack()
    bouton2 = Button(menu1,text = 'accéder au menu de stegannographie',command = lambda:os.system("python3 fonctions/steganographie_image/steganographie.py")).pack()
    bouton1 = Button(menu1,text = 'effectuer un filtre de niveaux de gris',command = lambda:os.system("python3 fonctions/steganographie_image/niveaux_de_gris.py")).pack()
    comfirmer = Button(menu1, text = 'quiter',command = lambda:menu1.quit()).pack()


    menu1.mainloop() # executer le premier menu 


menu_principal()

