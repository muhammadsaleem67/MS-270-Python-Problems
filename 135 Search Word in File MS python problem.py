def search_word(filename, target_word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Check if the word exists in the text
            if target_word in content:
                return True
            return False
    except FileNotFoundError:
        return False
target = "Muhammad Saleem"
print(search_word('python problem student marks.txt', target))