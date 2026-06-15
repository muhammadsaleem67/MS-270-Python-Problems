def replace_word(filename, old_word, new_word):
    try:
        # Step 1: Read the existing content
        with open(filename, 'r') as file:
            content = file.read()
        # Step 2: Replace the text in memory
        updated_content = content.replace(old_word, new_word)
        # Step 3: Write the updated content back, overwriting the file
        with open(filename, 'w') as file:
            file.write(updated_content)            
    except FileNotFoundError:
        print("File not found.")
word = "Muhammad Saleem"
newword = "Saleem"
replace_word('python problem student marks.txt', word, newword) # it updates te old word to new word in that file