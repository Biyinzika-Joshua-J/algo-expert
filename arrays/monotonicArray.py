def isMonotonic(nums):
        isDecreasing = True
        isIncreasing = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                isIncreasing = False
            if nums[i] > nums[i-1]:
                isDecreasing = False
        return isDecreasing or isIncreasing

