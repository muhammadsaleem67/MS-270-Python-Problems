def save_student_results(filename, student_data):
    with open(filename, 'w') as file:
        file.write("--- Student Results ---\n")
        
        # Iterate through the dictionary and write each line
        for name, score in student_data.items():
            file.write(f"Name: {name} | Score: {score}\n")
save_student_results('python problem student marks.txt', {"Muhammad Saleem": 97, "Babar Ali": 83} )
# it saves the info in txt file
"""
	1. Write Mode: We open a file in 'w' mode to build the report from scratch.
	2. Header: We write a static header.
	3. Formatting: We loop through the dictionary, formatting the name and score into a clean string using f-strings (f"..."), and write it line-by-line.
"""