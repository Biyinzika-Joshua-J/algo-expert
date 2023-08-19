def selectionSort(list):
    currentIdx = 0
    while currentIdx < len(list)-1:
        smallestIdx = currentIdx
        for i in range(currentIdx+1, len(list)):
            if list[smallestIdx] > list[i]:
                smallestIdx = i
        list[currentIdx], list[smallestIdx] = list[smallestIdx], list[currentIdx]
        currentIdx += 1
    return list
        




print(selectionSort([1002,-10,-123,0,1,93,21,42]))
