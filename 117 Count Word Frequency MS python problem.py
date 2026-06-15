def word_frequency(sentence):
    # Convert to lowercase and split into individual words
    words = sentence.lower().split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency
text = "apple banana apple cherry banana apple"
print(word_frequency(text))
# Output: {'apple': 3, 'banana': 2, 'cherry': 1}
