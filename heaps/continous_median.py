"""
repeat it

"""

import heapq
class MedianFinder(object):
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.median = None


    def addNum(self, num):
        if len(self.maxHeap) == 0 or num < -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        # check if the heaps need to be rebalanced
        self.rebalanceHeaps()
        # update median
        self.updateMedian()

    def rebalanceHeaps(self):
        if len(self.maxHeap) - len(self.minHeap) == 2:
            heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap))
        elif len(self.minHeap) - len(self.maxHeap) == 2:
            heapq.heappush(self.maxHeap, heapq.heappop(self.minHeap))
        

    def updateMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            self.median = (self.minHeap[0] + (-self.maxHeap[0]))/2
        elif len(self.minHeap) > len(self.maxHeap):
            self.median = self.minHeap[0]
        else:
            self.median = -self.maxHeap[0]

       

    def findMedian(self):
        return self.median
    
