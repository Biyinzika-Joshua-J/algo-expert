# uses constant space and linear time
def deleteDuplicates(self, head):
        currentNode = head
        while (currentNode):
            nextDistinctNode = currentNode.next
            while (nextDistinctNode and nextDistinctNode.val == currentNode.val):
                nextDistinctNode = nextDistinctNode.next
            currentNode.next = nextDistinctNode
            currentNode = nextDistinctNode
        return head

# use linear space and time
def deleteDuplicates2(self, head):
    seen = set()
    curr = head
    while (curr and curr.next):
        if not (curr.val in seen):
            seen.add(curr.val)
        if curr.next.val in seen:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
    