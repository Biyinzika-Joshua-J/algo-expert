"""
    involves adding up the depths of all nodes in BT..
"""
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

