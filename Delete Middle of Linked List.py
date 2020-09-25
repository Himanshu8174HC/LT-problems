def deleteMid(head):
    if head is None or head.next is None:
        return head
    le = 0
    cur = head
    while cur:
        le +=1
        cur = cur.next
    if le == 2:
        head.next = None
        return head
    k = (le//2)
    cur1 = head
    nxt = cur1
    l = 1
    
    while k:
        nxt= cur1
        cur1 = cur1.next
        k -=1
    nxt.next = cur1.next
    return head
