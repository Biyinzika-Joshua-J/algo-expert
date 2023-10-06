def removeNthFromEnd(self, head, n):
        if head is None:
            return head

        counter = 1
        first = head
        second = head
        while counter <= n: # NB: the second pointer is n nodes ahead
            second = second.next
            counter += 1

        if second is None and head.next: # means reached end of LL -> remove head
            head.val = head.next.val
            head.next = head.next.next
            return head
        elif second is None and head.next is None:
            return head.next
        
        while second.next is not None:
            second = second.next
            first = first.next

        first.next = first.next.next

        return head