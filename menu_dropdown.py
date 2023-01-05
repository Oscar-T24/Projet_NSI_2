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

# Create object
root = Tk()

# Adjust size
root.geometry( "200x200" )

# Change the label text
def show():
   label.config( text = clicked.get())
   try :
      image1 = Image.open('images/'+clicked.get())
      image1.resize((50,50))
      test = ImageTk.PhotoImage(image1)
      label1 = tkinter.Label(image=test)
      label1.image = test
      label1.place(x=50, y=50)
      #time.sleep(5)
      #label1.destroy()
   except FileNotFoundError:
      print('fichier inexistant')
      
   # Dropdown menu options

options = os.listdir('images')
options = [e for e in options if 'png' or 'jpg' or 'jpeg' in e and 'fusion.png' not in e]

   # datatype of menu text
clicked = StringVar()


   # initial menu text
clicked.set( "choisissez une photo" )

   # Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

   # Create button, it will change label text
button = Button( root , text = "choisir cette image" ,command = show).pack()


   # Create Label
label = Label(root , text = " " )
label.pack()



   # Execute tkinter

root.mainloop()