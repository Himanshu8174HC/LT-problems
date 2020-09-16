def findMid(head):
    count = 0
    pre = head

    while pre is not None:
        pre = pre.next
        count += 1
    k=(count//2)
    pre = head
    c=0
    while c!=k:
        pre = pre.next
        c+=1

    return pre.data
