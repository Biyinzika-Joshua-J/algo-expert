def twoSum(array, target): # the array has distict values
    hash = {}
    for idx, num in enumerate(array):
        if target-num not in hash:
            hash[num] = idx
        else:
            return [hash[target-num],idx]
    return [-1, -1]

print(twoSum([3,5,-4,8,11,1,-1,6], 10))