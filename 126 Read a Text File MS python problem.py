def read_file(filename):
    try:
        # 'r' stands for read mode
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
read_file('python problem.txt')

"""
	1. Error Handling: We wrap the code in a try-except block. If the file doesn't exist, Python will normally crash. The except FileNotFoundError catches this and prints a friendly error instead.
	2. Context Manager: with open(filename, 'r') as file: safely opens the file in read mode ('r').
	3. Reading: .read() grabs the entire contents of the file as a single massive string.
"""