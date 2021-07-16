class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        temp = ''
        
        while head:
            temp += str(head.val)
            head = head.next
        
        return int(temp, 2)
        
