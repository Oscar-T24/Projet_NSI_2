from cache_image_V4 import cache_image 
from retrouve_image_v4 import retrouve_image
from PIL import Image
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import time

im1 = Image.open('images/9.jpeg')
im2 = Image.open('images/10.png')
# faire un script qui donne une pop up pour selectionner une image dans 
# le catalogue ou qui passe par openAI pour génerer une image

def main():
    #ajouter un menu
    #cache_image OU retrouve_image en fonction de la demande de l'utilisateur
    cache_image(im1,im2,5)
    image_fusion = Image.open('images/fusion.png')
    time.sleep(2)
    retrouve_image(image_fusion,5)

#main()

def choisir_image():
   def retrouve():
       bits=passw_var.get()
       passw_var.set("")

       retrouve_image('images/'+clicked.get(),int(bits))
       
   def cache():
        bits=passw_var.get()
        passw_var.set("")
        cache_image('images/'+clicked.get(),'images/'+clicked2.get(),int(bits))
        
   menu1 = Tk()
   menu1.geometry( "300x600" )
   passw_var=StringVar()

   def image(image):
      if image == 2:
        label.config(text = clicked2.get())
        try :
         image2 = Image.open('images/'+clicked2.get()).resize((170,170))
         test2 = ImageTk.PhotoImage(image2)
         label2 = tkinter.Label(image=test2)
         label2.image = test2
         label2.place(x=75, y=415)
         #time.sleep(5)
         #label1.destroy()

        except FileNotFoundError:
         print('fichier inexistant')
      elif image == 1: 
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
   clicked2 = StringVar()
   clicked2.set( "choisissez une photo. laisser vide pour retrouver une image" )
   drop2 = OptionMenu( menu1 , clicked2 , *options )
   drop2.place(x=80, y=10)
   drop2.pack()

   # instatiation des boutons à partir de la classe Bouton
   label = Label(menu1 , text = " " )
   label.pack()
   label2 = Label(menu1 , text = " " )
   label2.pack()
   button = Button( menu1 , text = "précharger image 1" ,command = lambda:image(1)).pack() # .grid(row=1,column=0)
   button2 = Button( menu1 , text = "précharger image 2" ,command = lambda:image(2)).pack()
   reveler = Button(menu1,text = 'reveler une image',command = retrouve).pack()
   cacher = Button(menu1,text = 'cacher l"image 2 dans l"image 1',command = cache).pack()
   comfirmer = Button(menu1, text = 'fermer et commencer',command = lambda:menu1.quit()).pack()
   entree = Entry(menu1, textvariable = passw_var, font = ('calibre',10,'normal')).pack()

   menu1.mainloop() # executer le premier menu 

   return 'images/'+clicked.get(),'images/'+clicked2.get(),entree.get()

print(choisir_image())