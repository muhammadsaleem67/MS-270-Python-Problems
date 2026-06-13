def selection_sort(list):
    num = len(list)
    for i in range(num):
        # Assume the current starting element is the minimum
        min_idx = i
        # loop through the rest of the array to find the actual minimum
        for j in range(i+1, num):
            if list[j] < list[min_idx]:
                min_idx = j
        # swap the found minimum elemement with the element of the unsorted part
        list[i], list[min_idx] = list[min_idx], list[i]
    return list
print(selection_sort([34,56,76,45,34]))
"""
	1. Outer Loop: i tracks the boundary between the sorted front and the unsorted back.
	2. Finding the Minimum: We temporarily assume the number at i is the smallest (min_idx = i). Then, the inner loop checks every single remaining number. If it finds one even smaller, it updates min_idx.
	3. The Swap: Once the inner loop finishes, min_idx contains the index of the absolute smallest number remaining. We swap it with index i.
"""