def char_frequency(text):
    freq = {}   
    for char in text:
        # Ignore spaces for a cleaner result (optional)
        if char == " ":
            continue            
        freq[char] = freq.get(char, 0) + 1       
    return freq
print(char_frequency("hello world"))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
