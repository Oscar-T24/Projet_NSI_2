'''
#Import the required libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of the Tkinter library
win.geometry("700x350")

label = Label(win, text="Right-click anywhere to display a menu", font= ('Helvetica 18'))
label.pack(pady= 40)

#Add Menu
popup = Menu(win, tearoff=0)

#Adding Menu Items
popup.add_command(label="New")
popup.add_command(label="Edit")
popup.add_separator()
popup.add_command(label="Save")

def menu_popup(event):
   # display the popup menu
   try:
      popup.tk_popup(event.x_root, event.y_root, 0)
   finally:
      #Release the grab
      popup.grab_release()

win.bind("<Button-3>", menu_popup)

button = ttk.Button(win, text="Quit", command=win.destroy)
button.pack()

mainloop()
'''
# Import module
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os
import time

def choisir_image():
   menu1 = Tk()
   menu1.geometry( "300x300" )
   def show():
      label.config( text = clicked.get())
      try :
         initial = Image.open('images/'+clicked.get()).resize((170,170))
         test = ImageTk.PhotoImage(initial)
         label1 = tkinter.Label(image=test)
         label1.image = test
         label1.place(x=80, y=100)
         #time.sleep(5)
         #label1.destroy()

      except FileNotFoundError:
         print('fichier inexistant')
   options = os.listdir('images')
   options = [e for e in options if '.png' or '.jpg' or '.jpeg' in e and 'fusion.png' not in e]
   clicked = StringVar()
   clicked.set( "choisissez une photo" )
   drop = OptionMenu( menu1 , clicked , *options )
   drop.pack()
   # instatiation des boutons à partir de la classe Bouton
   button = Button( menu1 , text = "choisir cette image" ,command = show).pack()
   comfirmer = Button(menu1, text = 'fermer et commencer',command = lambda:menu1.quit()).pack()
   label = Label(menu1 , text = " " )
   label.pack()

   menu1.mainloop() # executer le premier menu 

   return 'images/'+clicked.get()

def menu_options():
   menu = Tk()
   menu.geometry( "300x300" )
   clicked = StringVar()
   clicked.set( "choisissez une photo" )
   bouton = Button( menu , text = "retrouver une image" ,command = retrouve_image).pack()
   bouton2 = Button(menu, text = 'cacher une image',command = cache_image).pack()
   label = Label(menu , text = " " )
   label.pack() 

   menu.mainloop() # executer le premier menu 
   
def retrouve_image():
   choisir_image
