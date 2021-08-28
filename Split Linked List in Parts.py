class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        ans = []
        sub_length = [(length // k)+1 if i < length % k else length // k for i in range(k)]
        
        for j in sub_length:
            if j == 0:
                ans.append(None)
            if j:
                ans.append(head)
                for _ in range(j-1):
                    head = head.next
                temp = head.next
                head.next = None
                head = temp
                
        return ans
        
        
