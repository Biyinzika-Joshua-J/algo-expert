"""
    used to find the maximum sum subarray.
    dynamic programming

   1=> maxEndingHere = max(maxEndingHere + num, num)
   2=> maxSoFar = max(maxSoFar, maxEndingHere)
"""

def kadanes(array): # O(N) time and O(1) space
    maxSoFar, maxEndingHere = [float(0), array[0]]
    for index in range(1, len(array)):
        maxEndingHere = max(maxEndingHere+array[index], array[index])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar 


print(kadanes([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]))  # ans => 19 [1,3,-2,3,4,7,2,-9]

