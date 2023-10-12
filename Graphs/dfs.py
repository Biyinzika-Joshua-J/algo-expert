class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    # O(V + E) time and O(V) space
    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        return array
    

