"""
array of only positive integers
greatest sum that can be generated without added 2 numbers next to each other in the array
"""
# O(N) time and space
def max_subset_sum(array):
    maxSums = [0 for sum in array]
    maxSums[0] = array[0]
    maxSums[1] = max(array[0], array[1])
    for idx in range(2, len(array)):
        maxSums[idx] = max(maxSums[idx-1], maxSums[idx-2] + array[idx])
    return maxSums[-1]

def optimized_space(array): # o(1) space
    second = array[0]
    first = max(array[0], array[1])
    for idx in range(2, len(array)):
        current = max(first, second + array[idx])
        second = first
        first = current
    return first


print(optimized_space([7,10,12,7,9,14])) # solution 7 + 12 + 14 = 33