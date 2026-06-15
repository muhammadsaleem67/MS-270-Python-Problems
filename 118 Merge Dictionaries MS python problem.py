def merge_dicts(dict1, dict2):
    # Python 3.9+ introduced the | operator for merging
    return dict1 | dict2
# For older Python versions, use dictionary unpacking:
    # return {**dict1, **dict2}
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
print(merge_dicts(d1, d2))
# Output: {'a': 1, 'b': 99, 'c': 3}
"""
	1. The Merge Operator (|): Introduced in Python 3.9, the "pipe" operator cleanly merges dictionaries.
	2. Overwriting: Notice the key "b". It existed in both dictionaries. Because d2 was placed on the right side of the merge, its value (99) won the conflict and overwrote the original 2.
"""