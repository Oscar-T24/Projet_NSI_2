import string
import sys

# The word to be encoded shifts by 5 to the right, while the word to be decoded shifts by 5 to the left.
#shift = 20
'''
print(' Caesar Cipher '.center(40, '*'))

choices = ['e', 'd']
user_choice = input('Do you wish to [e]ncode, [d]ecode, or quit (any other letter)?: ').lower()

if user_choice not in choices:
    print('Program closed.')
    sys.exit()

word = input('Enter the word: ')
'''

# ENCODING FUNCTION
def encode_words(words, shifts):
    """This encodes a word using Caesar cipher."""

    # Variable for storing the encoded word.
    encoded_word = ''

    for i in words:

        # Check for space and tab
        if ord(i) == 32 or ord(i) == 9:
            shifted_word = ord(i)

        # Check for punctuations
        elif i in string.punctuation:
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

        encoded_word = encoded_word + chr(shifted_word)
    return encoded_word
    #print('Word:', word)
    #print('Encoded word:', encoded_word)


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


def encode_decode(words, shifts, choice):
    """This checks if the users want to encode or decode, and calls the required function."""

    if choice == 'e':
        encode_words(words, shifts)
    elif choice == 'd':
        decode_words(words, shifts)

if __name__ == 'main':
    #encode_decode(word, shift, user_choice)
    pass