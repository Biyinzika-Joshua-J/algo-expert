"""
    Operations (core methods)
    -------------------------
    -Build heap 
        .using the siftdown method on every parent node in the heap starting at the last parent node
    -Sift down
        . compare the child nodes and swap with the smallest of them
    - Sift up
        . If parent is greater than the child, swap them
    -Insert
        . add to the last node in the heap
        . sift it up to its correct position (continously swaps inserted node with its parent nodes until it is in its right position) parent <= inserted_node --right pos
    -Remove
        . we remove the root node
            .swap the root node with the last value in the heap
            .pop the node at the end
            . call the sift down method
            . then recompute the child nodes of the node

    properties
    -----------
    => All its levels are completely filled from left to right.
    => Heap property -- every node that has a value is smaller than or equal to its children's nodes values for the min heap.

    useful formulas 
    ----------------
    current_node = index
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2
    parent_node = floor((i-1)/2)

    
"""
import math

class MinHeap:
    def __init__(self, array):
        self.heap = self.BuildHeap(array)

    def SiftUp(self, currentIdx, heap): # O(log(N)) time where n is the number of values in the binary heap
        parentIndex = math.floor((currentIdx-1)/2)
        if heap[parentIndex] > heap[currentIdx] and currentIdx > 0:
            self.Swap(parentIndex, currentIdx, self.heap)
            self.SiftUp(parentIndex, self.heap)
        return

    def SiftDown(self, currentIdx, endIdx, heap): # O(log(N)) time where n is the number of values in the binary heap
        leftChild = (2*currentIdx) + 1
        idxToSwap = None
        while leftChild <= endIdx:
            rightChild = (2*currentIdx) + 2 if (2*currentIdx) + 2 <= endIdx else -1
            if rightChild != -1 and heap[rightChild] < heap[leftChild]:
                idxToSwap = rightChild
            else:
                idxToSwap = leftChild
            if heap[idxToSwap] < heap[currentIdx]:
                self.Swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                leftChild = (2*currentIdx) + 1
            else:
                break
        
        

    def Insert(self, value): # O(log(N)) time where n is the number of values in the binary heap
        self.heap.append(value)
        self.SiftUp(len(self.heap)-1, self.heap)

    def Remove(self): # O(log(N)) time where n is the number of values in the binary heap
        self.Swap(0, len(self.heap)-1, self.heap)
        removedValue = self.heap.pop()
        self.SiftDown(0, len(self.heap)-1, self.heap)
        return removedValue

    def BuildHeap(self, array): # O(N) time where n is the number of values in the binary heap
        firstParentIdx = (len(array)-2) // 2
        for currentIdx in reversed(range(firstParentIdx)):
            self.SiftDown(currentIdx, len(array)-1, array)
        return array

    def Peek(self):
        return self.heap[0]

    def Swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


heap = MinHeap([9,6,14,5,1,-1,0,100])

result = []
while (len(heap.heap) != 0):
    result.append(heap.Remove())
print(result)
