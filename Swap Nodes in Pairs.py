class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        P = head
        new = head.next
        while head:
            Q = P.next
            temp = Q.next
            Q.next = P
            if temp == None or temp.next == None:
                P.next = temp
                break
            
            P.next = temp.next
            P = temp
        return new
    
