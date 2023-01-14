import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("images/10.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test,anchor= CENTER)
label1.pack(expand = True)
label1.image = test

# Position image
label1.place(x=0, y=0)
root.mainloop()