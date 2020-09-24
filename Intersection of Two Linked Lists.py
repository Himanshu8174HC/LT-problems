class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list1 = set()
        root1 = headA
        root2 = headB
        while root1 :
            list1.add(root1)
            root1 = headA.next
            headA = root1 
        while root2 :
            if root2 in list1 :
                return root2
            else :
                root2 = headB.next
                headB = root2
        return root2
        
        
############################################################MY Methode
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len1, len2 = 0, 0
        cur1 , cur2 = headA, headB
        while cur1:
            len1 += 1
            cur1 = cur1.next
        while cur2:
            len2 += 1
            cur2 = cur2.next
            
        while len1 > len2:
            headA = headA.next
            len1 -=1
            
        while len2 > len1:
            headB = headB.next
            len2 -=1
            
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
