# insertion
# deletion
# searching

"""
    left_node < parent_node <= right_node

    methods
    -------
    1.Insertion

    2.Searching

    3.Deletion (hardest)

    4.Traversal
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self # not relevant to the algorithm

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # many edge cases
                # 1. node with two children => find the smallest value of the right subtree..(left most value) subtree and replace it with the value you are trying to remove
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                #2. root node case without parent
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right
                        currentNode.left = currentNode.right.left
                    else:
                        currentNode.value = None
                #3
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                # 4
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.right if currentNode.right is not None else currentNode.left
                break
        return self
                



    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True

    def in_order_traversal(self, result=[]):
        if self is None:
            return result
        self.in_order_traversal(self.left, result)
        result.append(self.value)
        self.in_order_traversal(self.right, result)

    def post_order_traversal(self, result=[]):
        if self is None:
            return result
        result.append(self.value)
        self.in_order_traversal(self.left, result)
        self.in_order_traversal(self.right, result)
    def post_order_traversal(self, result):
        if self is None:
            return result
        self.in_order_traversal(self.left, result)
        self.in_order_traversal(self.right, result)
        result.append(self.value)





