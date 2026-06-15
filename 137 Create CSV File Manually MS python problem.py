def create_csv(filename, data_list):
    with open(filename, 'w') as file:
        # Write headers
        file.write("ID, Name, Department \n")

        # write data rows 
        for row in data_list:
            # convert elements to strings, join them with commas, add a new line
            row_string = "".join(str(item) for item in row)
            file.write(row_string + ",")
data_list = ["1", "Muhammad Saleem", "Computer Science"]
create_csv('python.csv', data_list)
"""
	1. Headers: Spreadsheets need column names. We write "ID,Name,Department\n".
	2. String Joining: For every list inside our main data list, we convert the items (like integers) into strings, and .join(",") them together. So [1, "Alice", "HR"] becomes "1,Alice,HR".
    Writing: We write that string to the file, ensuring we add \n to move to the next spreadsheet row.
"""