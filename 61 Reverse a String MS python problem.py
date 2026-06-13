def reverse_string(text):
    # Using Python's slice notation to step backward
    return text[::-1]

print(reverse_string("Python")) # Output: nohtyP
"""
Slice Notation: In Python, bracket slicing looks like `[start:stop:step]`.
2. The Trick: By leaving `start` and `stop` completely blank, we tell Python to look at the entire string. By making the `step` a `-1`, we tell it to read the string backward, one character at a time.
"""