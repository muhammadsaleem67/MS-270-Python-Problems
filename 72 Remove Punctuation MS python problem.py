import string
def remove_puntuation(text):
    # create an empty string to hold our result
    clean_text = ""
    for char in text:
        # string.puntuation contains all standards puntuation marks
        if char not in string.punctuation:
            clean_text += char
    return clean_text
print(remove_puntuation("Hello, World! How's it going?"))