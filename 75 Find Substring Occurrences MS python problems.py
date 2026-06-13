def count_substring(text, sub):
    # Python strings have a built-in method for this
    return text.count(sub)
print(count_substring("banana", "na")) # Output: 2
"""
	1. Built-in Efficiency: Python has a highly optimized .count() method for strings. You don't need to write a manual loop for this unless an interviewer specifically forces you to. It counts non-overlapping occurrences.
"""