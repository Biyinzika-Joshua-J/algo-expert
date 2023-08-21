"""
    height: non negative 0 integers..each value represents the building height,
    direction: in which these buildings are facing.. e.g EAST -> or WEST <- only

    return the indices of all the buildings taht can see the sunset and
    the array of the indices must be in asceeding order
"""

# O(N) time and 0(n) space if you consider the results array
def sunset_views_optimal(heights, direction):
    buildings = []
    maxHeight = float('-inf')
    maxHeightIndex = None
    if direction == 'EAST':
        # we start from west <-
        for i in reversed(range(0, len(heights))):
            if maxHeight < heights[i]:
                maxHeight = heights[i]
                maxHeightIndex = i
                buildings.append(maxHeightIndex)
        buildings.reverse()
    else:
        # we start from east ->
        for i in range(0, len(heights)):
            if maxHeight < heights[i]:
                maxHeight = heights[i]
                maxHeightIndex = i
                buildings.append(maxHeightIndex)
        
    return buildings

#my approach O(n^2) time and O(n) if you consider the results array
def sunset_views(heights, direction):  
    # approach - find the building with max height in sub arrays of i-n-1 continually
    buildings = []
    if direction == 'EAST':
        i = 0
        while i < len(heights):
            maxHeight = float('-inf')
            maxHeightIndex = 0
            for j in range(i, len(heights)):
                if maxHeight <= heights[j]:
                    maxHeight = heights[j]
                    maxHeightIndex = j
            buildings.append(maxHeightIndex)
            i = maxHeightIndex+1   
    else:
        i = len(heights)-1
        while i >= 0:
            maxHeight = float('-inf')
            maxHeightIndex = 0
            for j in reversed(range(0, i+1)):
                if maxHeight <= heights[j]:
                    maxHeight = heights[j]
                    maxHeightIndex = j
            buildings.append(maxHeightIndex)
            i = maxHeightIndex-1  
        buildings.reverse()
    return buildings


input = [3,5,4,4,3,1,3,2] # => [1,3,6,7]

print(sunset_views_optimal(input, 'WEST'))

