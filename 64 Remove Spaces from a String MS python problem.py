def remove_spaces(text):
    # Replace all spaces with an empty string
    return text.replace(" ", "")

print(remove_spaces("A B C D E")) # Output: ABCDE

"""
The `.replace()` Method: This method takes two arguments: what to look for, and what to replace it with.
The Swap: We tell it to look for `" "` (a space) and replace it with `""` (absolutely nothing), effectively deleting all spaces.
"""