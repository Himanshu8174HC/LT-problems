class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        S=None
        P=l1
        Q=l2
        
        if l1 and l2:
            if l1.val<=l2.val:
                S=P
                P=S.next
            else:
                S=Q
                Q=S.next
            new_head = S
        while P and Q:
            if P.val<=Q.val:
                S.next = P
                S = P
                P = S.next
            else:
                S.next = Q
                S =Q
                Q =S.next
        if not P:
            S.next = Q
        if not Q:
            S.next = P
        return new_head
