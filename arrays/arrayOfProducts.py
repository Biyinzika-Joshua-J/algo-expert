def arrayOfProducts(array):
    prefix = [0 for i in range(len(array))]
    suffix = [0 for i in range(len(array))]
    
    
    # generate prefix
    for idx in range(len(array)):
        if idx == 0:
            prefix[idx] = array[idx]
            continue
        prefix[idx] = array[idx] * prefix[idx-1]
    
     # generate suffix
    for idx in reversed(range(len(array))):
        if idx == len(array)-1:
            suffix[idx] = array[idx]
            continue
        suffix[idx] = array[idx] * suffix[idx+1]

    result = [i for i in range(len(array))]
    for idx in range(len(array)):
        if idx == 0:
            result[idx] = suffix[idx+1]
            continue
        if idx == len(array)-1:
            result[idx] = prefix[idx-1]
            continue
        result[idx] = prefix[idx-1] * suffix[idx+1]
    return result
    




test = [5, 1, 4, 2] # => [8, 40, 10, 20]
"""
    prefix = [5, 5, 5, 20]
    suffix = [40, 8, 2, 2]
    res = [8, 40, 10, 20]
"""
print(arrayOfProducts(test))