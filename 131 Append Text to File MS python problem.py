def append_to_file(filename, text_to_add):
    # 'a' stands for append mode
    with open(filename, 'a') as file:
        # \n ensures the new text starts on a fresh line
        file.write(f"\n{text_to_add}")
append_to_file('python problem append text.txt', "by Muhammad Saleem") 
# Output: by Muhammad Saleem ( written in the file python problem.txt )

"""
	1. Append Mode: Using 'a' tells Python to place the typing cursor at the very end of the file. (Using 'w' would erase the whole file first!).
    Writing: We use .write() to add the new text, prefixing it with \n (the newline character) so it doesn't get glued to the last word of the existing text.
"""