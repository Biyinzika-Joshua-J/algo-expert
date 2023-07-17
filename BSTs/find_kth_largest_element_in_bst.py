import bst_construction

def brute_force(bst, k):
    def generateSortedArray(root, array):
        if root is None:
            return
        generateSortedArray(root.left, array)
        array.append(root.value)
        generateSortedArray(root.right, array)
    sortedVals = []
    generateSortedArray(bst, sortedVals)
    return sortedVals[len(sortedVals)-k]

def find_kth_largest_element(bst, k): # do a reversed inorder traversal
    pass

bst = bst_construction.BST(10)
bst.insert(1).insert(100).insert(50).insert(25).insert(20).insert(11).insert(5).insert(9)
print(brute_force(bst, 3))
