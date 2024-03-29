class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0  
        elif not root.left and not root.right:
            return 1 
        elif not root.left:
            return self.minDepth(root.right)+1 
        elif not root.right:
            return self.minDepth(root.left)+1  
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1 

            
