# Make a script that generates an image based on the user input

import ImageDraw
import ImageFont
from PIL import Image

def generate(input):
    """
    input: string
    output: image
    Generate an image which reprensents the user's input
    """
    image = Image.new('RGB', (len(input)*10, 100), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 15)
    draw.text((0, 0), input, (0, 0, 0), font=font)
    image.save('images/generated.png', format = 'PNG')
    image.show()

generate(input('entrer un message ASCII à cacher'))


