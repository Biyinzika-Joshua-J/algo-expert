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


def bruteForce(array):
    minimumSecondIndex = len(array)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] == array[j] and i != j and i < j:
                minimumSecondIndex = min(minimumSecondIndex, j)
    return array[minimumSecondIndex] if minimumSecondIndex != len(array) else -1

#test = [2,1,1,5,3,3,2,4]
test = [1,2,3,4,5,6]
print(bruteForce(test))