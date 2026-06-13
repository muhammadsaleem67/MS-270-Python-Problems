def count_words(sentence):
    # .split() breaks the sentence into a list of words
    words_list = sentence.split()
    
    # len() counts how many items are in that list
    return len(words_list)

print(count_words("Coding in Python is awesome!")) # Output: 5

"""
1. Splitting: The `.split()` string method is incredibly powerful. By default (with empty parentheses), it hunts down every space, tab, or newline and chops the string apart at those points, creating a list of words.
2. Counting: We use the built-in `len()` function to count how many words ended up in that list.
"""
