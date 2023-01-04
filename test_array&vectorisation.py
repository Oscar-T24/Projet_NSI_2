import numpy as np
from PIL import Image

image = Image.open('images/1.jpg')
arr = np.array(image)
pixels = list(image.getdata())
carre = np.arange([255,255,255]).reshape(4, 3)
print(carre)
# pour s'inspirer : https://github.com/MathKode/stegano-video/blob/main/main.py 