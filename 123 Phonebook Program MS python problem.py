phonebook = {
    "Muhammad Saleem": "555-1234",
    "Bob": "555-9876"
}
def lookup_contact(name):
    # .get() returns None (or a custom message) if the key isn't found
    return phonebook.get(name, "Contact not found.")
def add_contact(name, number):
    phonebook[name] = number
    return f"{name} added successfully."
print(lookup_contact("Muhammad Saleem"))   # Output: 555-1234
print(lookup_contact("Babar Ali")) # Output: Contact not found.
"""
	1. Safe Lookup (.get()): If you try to access a dictionary using square brackets (phonebook["Charlie"]) 
    and the key doesn't exist, Python will crash with a KeyError. Using .get("Charlie", "Default Message") 
    is the professional way to handle missing keys without crashing.
"""