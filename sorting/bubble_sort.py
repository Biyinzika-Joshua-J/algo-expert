"""
    time complexity O(n^2)
    space complexity O(1)
"""

def bubbleSort(list):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                isSorted = False
    return list

def bubbleSortOptimized(list): # does not affect the time complexity
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(list)-1-counter):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                isSorted = False
        counter += 1
    return list

print(bubbleSortOptimized([3,1,100,-123,23,17,0,-923]))