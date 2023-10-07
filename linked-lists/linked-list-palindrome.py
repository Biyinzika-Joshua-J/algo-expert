def isPalindrome(head):
    fast = head
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next.next if fast.next is not None else None

    # reverse second half and get a ref to it
    p1 = None
    p2 = slow
    while p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3

    halfList1 = head
    halfList2 = p1
    while halfList1 and halfList2:
        if halfList1.val != halfList2.val:
            return False
        halfList1 = halfList1.next
        halfList2 = halfList2.next

    return True

# stack approach

# recursive approach

# reverse half of LL