import heapq
"""
    unsorted
"""
def laptopRentals(times): # max laptops the school needs for all students to have one when they need to rent out.
    times.sort(key=lambda x:x[0]) # nlogn
    laptops = 1
   
    return laptops

times = [[0,2], [1,4], [4,6], [0,4], [7,8], [4, 11], [3, 10]]

print(laptopRentals(times))

