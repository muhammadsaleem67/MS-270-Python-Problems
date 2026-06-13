def get_ascii_values(text):
    # Use a dictionary comprehension to map character -> ASCII value
    ascii_map = {char: ord(char) for char in text}
    return ascii_map
print(get_ascii_values("Cat")) 