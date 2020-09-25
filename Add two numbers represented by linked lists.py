def addLists(first, second):
    pre1 = None
    cur1 = first
    while cur1:
        nxt = cur1.next
        cur1.next = pre1
        pre1 = cur1
        cur1 = nxt
    first = pre1
    
    pre2 = None
    cur2 = second
    while cur2:
        nxt = cur2.next
        cur2.next = pre2
        pre2 = cur2
        cur2 = nxt
    second = pre2
   
    sum = 0
    cur = new = Node(0)
    while first or second or sum:
        if first:
            sum += first.data
            first = first.next
        if second:
            sum += second.data
            second = second.next
        cur.next = cur = Node(sum%10)
        sum=sum//10
    
    
    pre3 = None
    cur3 = new.next
    while cur3:
        nxt = cur3.next
        cur3.next = pre3
        pre3 = cur3
        cur3 = nxt
    new = pre3
    return new
   
