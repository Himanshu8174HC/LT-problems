  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or head.next is None:
            return None
        count = 0
        cur = head
        while cur:
            count+=1
            cur = cur.next
        
        if count == n:
            head= head.next
            return head
        pos = 1
        pre = head
        nxt = pre.next
        while pos<count - n:
            pre = nxt
            nxt = nxt.next
            pos +=1
        pre.next = nxt.next
        nxt.next = None
        return head
