def SquaredSort(array):
    startIdx = 0
    endIdx = len(array)-1
    result = [0 for _ in range(len(array))]
    for idx in reversed(range(len(array))):
        startIdxValue = array[startIdx]
        endIdxValue = array[endIdx]
        if abs(startIdxValue) > abs(endIdxValue):
            result[idx] = startIdxValue**2
            startIdx += 1
        else:
            result[idx] = endIdxValue**2
            endIdx -= 1
    return result

print(SquaredSort([-4,-3,-2,-1,0,1,2,3,4]))