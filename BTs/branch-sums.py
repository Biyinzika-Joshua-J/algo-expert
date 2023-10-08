def branchSums(root, sums=[], runningSum=0):
    if root is None:
        return
    if root.left is None and root.right is None:
        sums.append(runningSum)
        return sums

    return [branchSums(root.left, sums, runningSum + root.val), 
            branchSums(root.right, sums, runningSum + root.val)]
