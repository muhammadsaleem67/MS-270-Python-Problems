def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            # readlines() returns a list where each item is one line
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0
print(count_lines("python problem.txt"))
"""
	1. The .readlines() Method: Instead of reading the file as one giant string, .readlines() reads it line-by-line and stores each line as an item in a list.
    Counting: We just find the length of that list to get the line count.
"""