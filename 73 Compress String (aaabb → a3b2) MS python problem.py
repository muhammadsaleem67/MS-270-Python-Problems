def compress_string(thestring):
    if not thestring:
        return ""
    compressed = ""
    count = 1
    # loop from the second charactor to the end
    for i in range(1, len(thestring)):
        if thestring[i] == thestring[i - 1]:
            # if it's the same as the previous char, increase count
            count += 1
        else :
            # if it's different, append the previous char and its count
            compressed += thestring[i - 1] + str(count)
            count = 1 # Reset count for the new character
    # dont forget to append the very last sequence!
    compressed += thestring[-1] + str(count)

    return compressed
print(compress_string("aaabbcccd"))

"""
	1. Tracking State: We start a count at 1 because every character appears at least once.
	2. Look-Back Loop: We loop starting from index 1. We compare the current character s[i] to the one right behind it s[i-1].
	3. Building the String: When we hit a character that doesn't match the previous one, the "run" is over. We add the character and its total count to our result string, then reset the count back to 1.
The Final Catch: The loop ends when it checks the last character, but it hasn't added it yet. We must manually append the final character and its count at the very end.
"""