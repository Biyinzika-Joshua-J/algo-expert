def firstDuplicate(array):
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    return -1

def optimizedToConstantSpace(array): # since 1 >= x <= n
    for idx, num in enumerate(array):
        if (array[abs(num-1)] < 0):
            return abs(array[idx])
        newIndex = abs(num)-1
        array[newIndex] = -1*array[newIndex]
    return -1

test = [2,1,5,3,3,2,4]
print(optimizedToConstantSpace(test))