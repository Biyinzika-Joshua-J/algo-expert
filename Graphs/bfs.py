class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    # O(V + E) time and O(V) space
    def bfs(self, array):
        queue = [self]

        while len(queue) != 0:
            currentNode = queue.pop(0)
            array.append(currentNode.name)
            for child in currentNode.children:
                queue.append(child)
        return array

        

    

