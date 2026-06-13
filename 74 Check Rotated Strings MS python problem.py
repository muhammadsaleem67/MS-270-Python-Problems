def  is_rotation(str1, str2):
    # if lengths are different, they can't be rotations 
    if len(str1) != len(str2):
        return False
    # Concretenate str1 to itself and check if str2 is inside it 
    combined = str1 + str2
    return str2 in combined
print(is_rotation("waterbottle", "erbottlewat"))
print(is_rotation("hello", "lloeh"))
"""
	1. Length Check: Rotated strings must have the exact same number of characters.
	2. The Concatenation Trick: This is a famous algorithmic shortcut. If you take a string and glue it to itself ("waterbottlewaterbottle"), it will contain every possible rotation of that string within it.
	3. Substring Check: We use the in keyword to ask Python if str2 exists anywhere inside our doubled str1.
"""