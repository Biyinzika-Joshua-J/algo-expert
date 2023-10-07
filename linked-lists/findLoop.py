# assumes that the loop is not their as well-->more error prone
def detectCycle(self, head):
    first = second = head
    while second and second.next:
        first = first.next
        second = second.next.next
        if first == second: break
    else: return None  # if not (fast and fast.next): return None
    while head != first:
        first = first.next
        head = head.next
    return first

# this assumes that the loop always exists
def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first

# using linear space
def detectCycleBruteForce(self, head):
    seen = set()
    curr = head
    while curr:
        if curr in seen:
            return curr
        seen.add(curr)
        curr = curr.next
    return curr


    