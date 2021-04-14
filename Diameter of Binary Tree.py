class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        def helper(root):
            nonlocal ans 
            if not root:
                return 0
            
            R = helper(root.right)
            L =  helper(root.left)
            
            ans = max (ans, L + R +1)
            return max(L, R)+1
        
        
        helper(root)
        return ans-1
            
