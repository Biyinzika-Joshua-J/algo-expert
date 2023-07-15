def three_sum(array, target):
    result = []
    array.sort()
    for idx, value in enumerate(array):
        left = idx+1
        right = len(array)-1
        while left < right:
            sum = value + array[left] + array[right]
            if sum == target:
                result.append([value, array[left], array[right]])
                left += 1
                right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1
    return result

print(three_sum([12,3,1,2,-6,5,-8,6], 0))

