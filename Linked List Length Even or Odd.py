def isLengthEvenOrOdd(head):
    count = 1
    while head:
        count += 1
        head = head.next
    return count%2
        
