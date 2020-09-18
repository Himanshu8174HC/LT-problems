class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head
        nxt = head.next
        while nxt is not None:
            if cur.val == nxt.val:
                cur.next = nxt.next
            else:
                cur = cur.next
            nxt = nxt.next
                
        return head
