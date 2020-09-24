class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        P = head
        new = P.next
        while 1:
            Q = P.next
            temp = Q.next
            Q.next = P
            if temp == None or temp.next == None:
                P.next = temp
                break
            else:
                P.next = temp.next
                P = temp
        return new
    
    
