def find_longest_word(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    # Use the max functions, telling it to compare based on length
    longestword = max(words, key = len)
    return longestword
print(find_longest_word("Python is amazing programming language"))
