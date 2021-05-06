class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
      temp = []
      while head:
        temp.append(head.val)
        head = head.next
      def tree(i, j):
        if i <= j:
          m = (i+j) // 2
          t = TreeNode(temp[m])
          t.left = tree(i, m-1)
          t.right = tree(m+1, j)
          return t
      return tree(0, len(temp)-1)
        
