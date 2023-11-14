"""
    product sum is the sum all on elems in the array but if the elems are in nested array you
    sum up the nums in the array and multiply by the depth of that special array.
    NB: The initial array has a depth of 1

    [depth 1 [depth 2] [depth 2 [depth 3]]]
"""
# O(N) time where is N is all the element and sub arrays in the array and O(D) space where D is the depth of the deepest array
def product_sum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) is list:
            # recursive call
            sum += product_sum(element, multiplier+1)
        else:
            sum += element
    return sum * multiplier

input1 = [5,2,[7,-1], 3, [6,[-13, 8],4]] # 12

print(product_sum(input1))