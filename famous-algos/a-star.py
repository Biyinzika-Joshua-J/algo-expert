class Node:
    def __init__(self, row, col, value):
        self.id = str(row) + '-'+str(col)
        self.row = row
        self.col = col
        self.value = value
        self.distanceFromStart = float('inf') # G score
        self.estimatedDistanceToEnd = float('inf') # hueristic value.(Gues how long it will take to get to the end node)
        self.cameFrom = None

def initializeNodes(graph):
    nodes = []
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i, j, value))
    return nodes

def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endCol = endNode.col
    return abs(endRow-currentRow) + abs(endCol-currentCol)

def getNeighboringNodes(node, nodes):
    neighbors = []
    numRows = len(nodes)
    numCols = len(nodes[0])
    row = node.row
    col = node.col

    if row < numRows-1: # down
        neighbors.append(nodes[row + 1][col])

    if row > 0: # up
        neighbors.append(nodes[row-1][col])

    if col < numCols-1: # right
        neighbors.append(nodes[row][col+1])

    if col > 0: # left
        neighbors.append(nodes[row][col-1])

    return neighbors





def A_star(startRow, startCol, endRow, endCol, graph):
    nodes = initializeNodes(graph)
    startNode = nodes[startRow, startCol]
    endNode = nodes[endRow, endCol]

    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)

    nodesToVisit = MinHeap([startNode]) #priority queue to keep track of minimum F (predicted) distance

    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove()
        if currentMinDistanceNode == endNode:
            break
        neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)

        for neighbour in neighbors:
            if neighbour.value == 1:
                continue
            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart+1

            if tentativeDistanceToNeighbor >= neighbour.distanceFromStart:
                continue
            neighbour.cameFrom = currentMinDistanceNode

            neighbour.distanceFromStart = tentativeDistanceToNeighbor
            neighbour.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance(neighbour,endNode)

            if not nodesToVisit.contains(neighbour):
                nodesToVisit.insert(neighbour)
            else:
                nodesToVisit.update(neighbour)

    return rescontructPath(endNode)

def rescontructPath(endNode):
    if not endNode.cameFrom:
        return []
    
    currentNode = endNode
    path = []

    while currentNode:
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom

    return path[::-1]


 

 # min Heap--algoExpert minHeap construction
class MinHeap: # minute 45:30
    def __init__(self, array):
        self.nodePositionsInHeap = {node.id:idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def buildHeap(self, array):
        firstParentIdx = (len(array)-2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array
    
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx *2+2 <= endIdx else -1
