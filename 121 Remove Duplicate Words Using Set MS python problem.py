def remove_duplicates(sentence):
    words = sentence.split()    
    # Convert list to a set to automatically drop duplicates
    unique_words = set(words)
    # Join back into a string
    return " ".join(unique_words)
print(remove_duplicates("hello world hello python world"))
# Output: 'world python hello' (Note: order is randomized!)
"""
	1. List to Set: Sets are a mathematical data structure in Python that inherently cannot contain duplicate items. Casting the list of words into a set() instantly destroys any repeats.
	2. The Trade-off: Standard sets do not remember the order items were added. When you join them back into a string, the sentence will likely be scrambled.
"""