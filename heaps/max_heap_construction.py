"""

"""

class MaxHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIdx = (len(array)-2)//2
        for idx in reversed(range(firstParentIdx+1)):
            self.siftDown(idx, len(array)-1, array)
        return array

    def siftUp(self, currentIdx, heap):
        while currentIdx > 0:
            parentIndex = (currentIdx-1)//2
            if heap[currentIdx] > heap[parentIndex]:
                self.swap(currentIdx, parentIndex, heap)
                currentIdx = parentIndex
            else:
                break

    def siftDown(self, currentIdx, endIdx, heap):
        leftChild = (2*currentIdx)+1
        idxToSwap = None
        while leftChild <= endIdx:
            rightChild =  (2*currentIdx)+2 if  (2*currentIdx)+2 <= endIdx else -1
            if rightChild != -1 and heap[rightChild] > heap[leftChild]:
                idxToSwap = rightChild
            else:
                idxToSwap = leftChild
        
            if heap[idxToSwap] > heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                leftChild = (2*currentIdx)+1
            else:
                break

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        removedValue = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return removedValue

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    def peek(self):
        return self.heap[0]
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


#heap = MaxHeap([-1,2,100,-100,30,40,14,138]) # bug
heap = MaxHeap([-1,2,100,-100,30,10000,40,14,128, 220, 180,300]) #  correct

print(heap.heap)

result = []
while (len(heap.heap) != 0):
    result.append(heap.remove())
print(result)
