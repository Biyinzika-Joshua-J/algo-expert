"""
    not optimal
    time: O(n^2)
    space: O(1)
"""

def insertionSort(list):
    for i in range(1, len(list)):
        j = i
        while j > 0 and list[j] < list[j - 1]:
            list[j], list[j - 1] = list[j - 1], list[j]
            j -= 1
    return list

print(insertionSort([848,-19,93,0,-10,1,2]))

