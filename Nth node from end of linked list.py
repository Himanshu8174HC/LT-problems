def getNthfromEnd(head,n):
    count=0
    cur = head
    while cur:
        count+=1
        cur = cur.next
    if n>count or head is None:
        return -1
    
    pos = 0
    pre = head
    while pos<count - n:
        pos+=1
        pre= pre.next
    return pre.data
