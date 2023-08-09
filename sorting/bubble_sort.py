def bubbleSort(list):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                isSorted = False
    return list

print(bubbleSort([3,1,100,-123,23,17,0,-923]))