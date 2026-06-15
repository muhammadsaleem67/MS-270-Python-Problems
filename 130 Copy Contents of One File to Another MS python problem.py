def copy_file(source, destination):
    try:
        # Open source in read mode, and destination in write mode
        with open(source, 'r') as src_file, open(destination, 'w') as dest_file:
            content = src_file.read()
            dest_file.write(content)
        print("Copy successful!")
    except FileNotFoundError:
        print("Source file not found.")
copy_file('python problem.txt', 'C:/Users/Muhammad Saleem/Desktop/Programming/Python Project/Python')
"""
	1. Multiple Files: The with open() statement can handle multiple files at once. We open the source as 'r' (read) and the destination as 'w' (write). Note: 'w' mode will overwrite the destination file if it already exists, or create a new one if it doesn't.
Transfer: We read the src_file into a variable, then immediately .write() that variable into the dest_file.
"""