class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val = node.next.val
            if node.next.next:
                node = node.next
            else:
				# tail
                node.next = None
###################################2nd Solution

node.val = node.next.val
node.next = node.next.next
