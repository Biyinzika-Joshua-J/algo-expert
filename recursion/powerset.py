"""
powerset is the set of all subsets of a set
order of the subsets doesn't matter
"""

def powerset(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            currentSubSet = subsets[i]
            subsets.append(currentSubSet + [num])
    return subsets