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
    
################################################BEST 
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        number = 0
        reverse = 0
        
        curr = head
        multiplier = 1
        while(curr):
            number = number * 10 + curr.val # append curr.val to the end of number
            reverse = curr.val * multiplier + reverse # append curr.val to the beginning of reverse
            
            curr = curr.next
            multiplier *= 10
            
