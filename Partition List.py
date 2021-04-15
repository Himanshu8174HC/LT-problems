class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        temp1 = ListNode()
        temp2 = ListNode()
        
        t1 = temp1
        t2 = temp2
        
        while head:
            if head.val < x:
                t1.next = head
                t1 = t1.next
            else:
                t2.next = head
                t2 = t2.next
                
            head = head.next
        
        t1.next = temp2.next
        t2.next = None
        return temp1.next
                
