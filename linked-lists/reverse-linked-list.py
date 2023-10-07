def reverseList(head):
    pointerOne = None
    pointerTwo = head
    pointerThree = head

    while pointerTwo is not None:
        pointerThree = pointerTwo.next
        pointerTwo.next = pointerOne
        pointerOne = pointerTwo
        pointerTwo = pointerThree
    return pointerOne
    
