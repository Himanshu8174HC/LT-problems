class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        l = []
        while head:
            l.append(head.val)
            head = head.next
        if l == l[::-1]:
            return True
        return False
