# import tkinter module
from tkinter import * 
from tkinter.ttk import *

# creating main tkinter window/toplevel
master = Tk()

# this will create a label widget
l1 = Label(master, text = "choisissez une premiere image")
l2 = Label(master, text = "choisissez une seconde image")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# entry widgets, used to take entry from user
e1 = Button(master,text = 'lol',command = lambda:master.quit())
e2 = Entry(master, text = 'entrer le nnombre de bits de poids fort')

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 5)
e2.grid(row = 1, column = 1, pady = 2)

# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
