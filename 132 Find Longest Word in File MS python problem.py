def longest_word_in_file(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            if not words:
                return None
            # Use max() with key=len to find the longest word
            return max(words, key=len)
    except FileNotFoundError:
        return None
print(longest_word_in_file('python problem.txt'))