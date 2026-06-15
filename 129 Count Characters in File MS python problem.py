def count_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # len() on a string counts every character, including spaces and newlines
            return len(content)
    except FileNotFoundError:
        return 0
print(count_characters('python problem.txt'))