class Solution(object):
    def sumRootToLeaf(self, root):
        
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, val):
            if root is None:
                return 0
            val = val*2 + root.val
            
            if not root.left and not root.right:
                return val
            return helper(root.left, val) + helper(root.right, val)
        return helper(root, 0)
        
