def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Split the text by whitespace to get a list of words
            words = content.split()
            return len(words)
    except FileNotFoundError:
        return 0
print(count_words('python problem.txt'))
"""
	1. Reading: We read the whole file into a string.
	2. Splitting: .split() automatically breaks the string apart at every space, tab, or newline, turning it into a list of individual words.
    Counting: len(words) counts how many items are in that list.
"""