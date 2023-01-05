import numpy as np
from PIL import Image

def flou(image,rayon):
 # Convert the image to a NumPy array
    image_array = np.array(image)
    print(image_array)
    rayon = 0
    # # Compute the window size
    window_size = 2 * rayon + 1

    # # Create a zero array for the output image
    output_array = np.zeros_like(image_array)

    # # Iterate over the image, skipping the border pixels
    for i in range(rayon, image.height - rayon):
        for j in range(rayon, image.width - rayon):
    #         # Extract the current window
            window = image_array[i - rayon: i + rayon + 1, j - rayon: j + rayon + 1]
    #         # Compute the average of the window
            avg = window.mean(axis=(0, 1))
    #         # Set the pixel value in the output image
            output_array[i, j] = avg

    # # Convert the output array back to an image
    output_image = Image.fromarray(output_array)
    output_image.show()
        
image = Image.open('images/10.png')   
image.show()
flou(image,14)