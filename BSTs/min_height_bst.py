import bst_construction
import math


def min_height_bst(sorted_array): # construct bst with min height from the array - distinct integers
    return constructBST(sorted_array, None, 0, len(sorted_array)-1)

def constructBST(array, bst, startIdx, endIdx):
    # base case
    if endIdx < startIdx:
        return
    middle = (startIdx+endIdx)//2
    valueToAdd = array[middle]
    if bst is None:
        bst = bst_construction.BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    constructBST(array, bst, startIdx, middle-1)
    constructBST(array, bst, middle+1, endIdx)
    return bst


print(min_height_bst([1,2,5,7,10,13,14,15,22]).__dict__)