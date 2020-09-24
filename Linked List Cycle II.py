class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow:
                    if slow == fast:
                        return slow
                    slow = slow.next
                    fast = fast.next
        return None
        
 
