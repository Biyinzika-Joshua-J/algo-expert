# O(max(l1,l2)) + 1 time and space
def addTwoNumbers(self, l1, l2):
    newLinkedListHeadPointer = ListNode(0)
    currentNode = newLinkedListHeadPointer
    carry = 0

    node1 = l1
    node2 = l2

    while (node1 or node2 or carry != 0):
        value1 = node1.val if node1 is not None else 0
        value2 = node2.val if node2 is not None else 0
        sumOfValues = value1 + value2 + carry

        newValue = sumOfValues % 10
        newNode = ListNode(newValue)
        currentNode.next = newNode
        currentNode = currentNode.next

        carry = sumOfValues // 10

        node1 = node1.next if node1 is not None else None
        node2 = node2.next if node2 is not None else None

    return newLinkedListHeadPointer.next


# O(m + n) time and space
def addTwoNumbersBruteForce(self, l1, l2):
    num1 = ''
    num2 = ''

    curr = l1
    while curr:
        num1 += str(curr.val)
        curr = curr.next

    curr = l2
    while curr:
        num2 += str(curr.val)
        curr = curr.next

    num1 = int(num1[::-1])
    num2 = int(num2[::-1])

    res = str(num1 + num2)[::-1]

    # create linked list
    head = ListNode(res[0])
    current = head
    for idx in range(1, len(res)):
        value = res[idx]
        current.next = ListNode(value)
        current = current.next

    return head
