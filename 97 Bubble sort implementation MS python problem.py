def bubble_sort(list):
    num = len(list)
    for i in range(num):
        # flag to check if any swaps happen in this pass
        swapped = False
        for j in range(0, num - i - 1):
            if list[j] > list[j +1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        # if no two elements were swapped, the list is already sorted!
        if not swapped:
            break
    return list
print(bubble_sort([64,56,76,45,12,65,34]))
"""
	1. The Nested Loops: The outer loop dictates how many passes we make. The inner loop compares adjacent elements (lst[j] and lst[j + 1]).
	2. The Optimization (- i): After each full pass, the largest number "bubbles" to the correct spot at the end. We use n - i - 1 so we don't waste time checking the already-sorted end of the list.
	3. The Early Exit (swapped): If we complete a full pass without making a single swap, the list is perfectly sorted. We break the loop early to save processing power.
"""