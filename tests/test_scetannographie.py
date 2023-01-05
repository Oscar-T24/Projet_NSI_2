#https://math.univ-lyon1.fr/irem/Formation_ISN/formation_prog_images/module_PIL/stegano_PIL.html

from PIL import Image


def fusionne(n, m) :
	return (n//16)*16 + (m//16)
	# ou return  (n & 0b11110000) | (m >> 4)


# ouverture de l'image qui restera apparente :
imageVisible = Image.open('images/logoIsnIrem.png')
# ouverture de l'image à cacher dans l'autre (mêmes dimensions que la précédente) :
imageACacher = Image.open('images/logoPython.png')

# création d'une image de mêmes dimensions :
imageFusion = Image.new('RGB', imageVisible.size)



listePixelsVisible = list(imageVisible.getdata())
listePixelsACacher = list(imageACacher.getdata())
listePixelsFusion = []


for i, (r, g, b) in enumerate(listePixelsVisible) :
	r0, g0, b0 = listePixelsACacher[i]
	listePixelsFusion.append( (fusionne(r,r0) ,fusionne(g,g0) ,fusionne(b,b0)) )


imageFusion.putdata(listePixelsFusion)
# on lance une visualisation :
imageFusion.show()
# sauvegarde de l'image   :
imageFusion.save('fusion.png')