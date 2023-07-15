def moveElementToEnd(array, element): # in place solution
    left = 0
    right = len(array)-1

    while left < right:
        while left < right and array[right] == element:
            right -= 1
        if array[left] == element:
            array[left], array[right] = array[right], array[left]
        left += 1
    return array


test = [2,1,2,2,2,3,4,2]

print(moveElementToEnd(test, 2))