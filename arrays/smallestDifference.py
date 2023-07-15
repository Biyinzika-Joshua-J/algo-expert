def smallest_difference(array1, array2): # => [num1, num2] smallest diff pair
    array1.sort()
    array2.sort()
    pointer1, pointer2 = (0,0)
    difference = float('inf')
    pair = [0,0]

    while (pointer1 < len(array1) and pointer2 < len(array2)):
        if array1[pointer1] == array2[pointer2]:
            return [array1[pointer1], array2[pointer2]]
        elif array1[pointer1] < array2[pointer2]:
            diff = array2[pointer2] - array1[pointer1]
            if (diff < difference):
                difference = diff
                pair = [array2[pointer2], array1[pointer1]]
            pointer1 += 1
        else:
            diff = array1[pointer1] - array2[pointer2]
            if (diff < difference):
                difference = diff
                pair = [array1[pointer1], array2[pointer2]]
            pointer2 += 1
    return pair

        

array1 = [-1,5,10,20,28,3]
array2 = [26,134,135,15,17]
print(smallest_difference(array1, array2))