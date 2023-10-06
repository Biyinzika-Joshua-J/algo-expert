"""

"""

def max_sum_increasing_subset(array):
    greatestSums = [0 for i in array]
    greatestSums[0] = array[0]
    greatestSums[1] = max(array[0], array[0]+array[1])

    print(greatestSums)

print(max_sum_increasing_subset([18, 12, 2, 3, 15, 5, 7])) # 8 + 12 + 15 = 35