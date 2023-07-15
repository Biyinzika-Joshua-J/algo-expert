def spiral_travel(array): # return values in spirat order
    result = []
    startCol, lastCol = (0, len(array[0])-1)
    lastRow = len(array)-1
    startRow = 0

    while startCol < lastCol and startRow < lastRow:
        # traverse start row
        for i in range(startCol, lastCol+1):
            result.append(array[startRow][i])
        startRow += 1
        # traverse right edge 
        for i in range(startRow, lastRow):
            result.append(array[i][lastCol])
        # traverse last row
        for i in reversed(range(startCol, lastCol+1)):
            result.append(array[lastRow][i])
        lastRow -= 1
        # traverse left edge
        for i in reversed(range(startRow, lastRow+1)):
            result.append(array[i][startCol])

        # update start and last
        startCol += 1
        lastCol -= 1

    
    return result



array = [
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10, 9, 8, 7]
    ]

print(spiral_travel(array))