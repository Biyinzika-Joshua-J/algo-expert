def arrayOfProducts(array):
    prefix = [1 for i in range(len(array))]
    suffix = [1 for i in range(len(array))]
    
    
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
    
    print(prefix)
    print(suffix)

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
    


# better space - O(n)
def optimized(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return products


test = [5, 1, 4, 2] # => [8, 40, 10, 20]
"""
    prefix = [5, 5, 5, 20]
    suffix = [40, 8, 2, 2]
    res = [8, 40, 10, 20]
"""
print(arrayOfProducts(test))