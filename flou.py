from PIL import Image

image = Image.open('chien.png')
image = image.resize((300, 300))
rgb_im = image.convert('RGB')
print('taille =', image.width, image.height)

for e in range(0,image.width):
    for e2 in range(0,image.height):
        r, g, b= rgb_im.getpixel((e, e2))
        rgb_im.putpixel( (e, e2), (g, 255-r, b, 0) )

#rgb_im = rgb_im.resize((500, 500))
rgb_im.show()
