def insertInMid(head,node):
    #code here
    
    curr = head
    prev = None
    if (head == None):
        head = node
        return head
    
    
    if n%2 == 0:
        count = n//2
    else:
        count = n//2+1
    n1 = 0
    curr = head
    while n1 != count :
        prev = curr
        curr = curr.next
        n1 = n1+1
    
    prev.next = node
    node.next = curr
    return head
