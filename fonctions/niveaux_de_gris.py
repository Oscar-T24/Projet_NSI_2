
from PIL import Image
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

def niveaux_de_gris(image):
    '''
    image --> image
    renvoie une image en noir et blanc
    '''
    final = Image.new('RGB',(image.size))
    lar,lon = image.width , image.height
    for x in range (lar):
        for y in range (lon):
            try:
                r,g,b = image.getpixel((x,y))
            except ValueError:
                r,g,b,t = image.getpixel((x,y))
            moyenne_gris = round((r+g+b)/3)
            final.putpixel((x,y),(moyenne_gris,moyenne_gris,moyenne_gris))
    final.save('images/niveaux_de_gris.png')

    image1_size = image.size
    image2_size = final.size
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image,(0,0))
    new_image.paste(final,(image1_size[0],0))
    new_image.save("images/niveaux_de_gris","PNG")
    new_image.show()
            
def choisir_image():   
    menu1 = Tk()
    menu1.geometry( "200x400" )
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
    reveler = Button(menu1,text = 'effectuer un filtre niveau de gris',command = lambda:niveaux_de_gris(Image.open('images/'+clicked.get())))
    reveler.grid(row = 2, column = 0, pady = 5)
    comfirmer = Button(menu1, text = 'fermer cette fenetre',command = lambda:menu1.quit())
    comfirmer.grid(row = 4, column = 0, pady = 5)
    #entree = Entry(menu1, textvariable = passw_var, font = ('calibre',10,'normal'))
    #ntree.grid(row = 5,column = 0,pady = 5)
 
    menu1.mainloop() # executer le premier menu 

    return 

choisir_image()