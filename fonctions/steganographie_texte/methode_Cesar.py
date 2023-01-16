import string
import sys


def encode_words(words, shifts):
    """encoder un message ASCII en Cesar """
    mot_encode = ''
    for i in words:
        if ord(i) == 32 or ord(i) == 9 or i in string.punctuation: # verifie les espaces et les tabs : ne pas ajouter de shifts pour ces caracteres ; si il y a de la ponctuation, ne pas shifter le caractere
            shifted_word = ord(i)
        # Check if the character is lowercase or uppercase
        elif i.islower():
            shifted_word = ord(i) + shifts
            # Lowercase spans from 97 to 122 (decimal) on the ASCII table
            # If the chars exceeds 122, we get the number it uses to exceed it and add to 96 (the character before a)
            if shifted_word > 122:
                shifted_word = (shifted_word - 122) + 96
        else:
            shifted_word = ord(i) + shifts

            # Uppercase spans from 65 to 90 (decimal) on the ASCII table
            # If the chars exceeds 90, we get the number it uses to exceed it and add to 64 (the character before A)
            if shifted_word > 90:
                shifted_word = (shifted_word - 90) + 64

        mot_encode = mot_encode + chr(shifted_word)
    return mot_encode

# DECODING FUNCTION
def decode_words(words, shifts):
    """This decodes a word using Caesar cipher"""

    # Variable for storing the decoded word.
    decoded_word = ''

    for i in words:

        # Check for space and tab
        if ord(i) == 32 or ord(i) == 9:
            shifted_word = ord(i)

        # Check for punctuations
        elif i in string.punctuation:
            shifted_word = ord(i)

        # Check if the character is lowercase or uppercase
        elif i.islower():
            shifted_word = ord(i) - shifts

            # If the char is less 122, we get difference subtract from 123 (the character after z)
            if shifted_word < 97:
                shifted_word = (shifted_word - 97) + 123

        else:
            shifted_word = ord(i) - shifts

            # If the char is less 65, we get difference and subtract from 91 (the character after Z)
            if shifted_word < 65:
                shifted_word = (shifted_word - 65) + 91

        decoded_word = decoded_word + chr(shifted_word)
    return decoded_word
    #print('Word:', word)
    #print('Decoded word:', decoded_word)
