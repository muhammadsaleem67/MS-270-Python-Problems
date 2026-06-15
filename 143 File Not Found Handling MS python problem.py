def read_secure_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Alert: The file '{filename}' is missing!"
print(read_secure_file("python problem passwors.txt")) 