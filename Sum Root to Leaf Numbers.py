class Solution(object):
    def sumNumbers(self, root):
        
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(root, total):
            if root is None:
                return 0
            
            total = total*10 + root.val
            
            if not root.left and not root.right:
                
                return total
            return helper(root.left, total) + helper(root.right, total)
        return helper(root, 0)
        
