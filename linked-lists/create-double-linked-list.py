class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = Node(val)
        else:
            # add to the end
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
            newNode.prev = curr
            self.head = newNode
        
        return self

    def RemoveNode(self, index):
        pass


list = [1,2,3,4,5]

dd = DoubleLinkedList()
for num in list:
    dd.append(num)

print(dd.val)