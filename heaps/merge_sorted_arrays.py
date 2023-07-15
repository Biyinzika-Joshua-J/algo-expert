import heapq


def merge(lists):
    pointers = [0]*len(lists)
    lengths = [len(list) for list in lists]
    result = []
    while not areAllPointersOutOfBound(pointers, lengths):
        minHeap = [(lists[pointer_idx][pointer], pointer_idx) for pointer_idx, pointer in enumerate(pointers) if pointer < lengths[pointer_idx]]
        heapq.heapify(minHeap)
        minimumValue, minimumValuePointerIndex = heapq.heappop(minHeap)
        result.append(minimumValue)
        pointers[minimumValuePointerIndex] += 1
    return result


def areAllPointersOutOfBound(pointers, lengths):
    for index in range(len(lengths)):
        pointer = pointers[index]
        length = lengths[index]
        if pointer < length:
            return False
    return True

lists = [
    [1,5,9,21],
    [-1,0],
    [-124,81,121],
    [3,6,12,20,150],
]

print(merge(lists))
print(mergeBruteForce(lists))