def count_votes(votes_list):
    tally = {}
    for vote in votes_list:
        # We can use .get() here as a shortcut for the if/else logic!
        # It fetches the current score, defaulting to 0 if the candidate is new, then adds 1
        tally[vote] = tally.get(vote, 0) + 1
    return tally
ballot_box = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
results = count_votes(ballot_box)
print(results)
# Output: {'Alice': 3, 'Bob': 2, 'Charlie': 1}
"""
The .get() Trick: This is a much faster way to write the logic from problem #117. tally.get(vote, 0) 
says: "Give me the current score for this candidate. If they aren't in the dictionary yet, give me a 0." 
We then immediately add 1 to that number and save it back to the dictionary.
"""