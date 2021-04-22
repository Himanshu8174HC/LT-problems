class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
     
      if not root:
        return []
        
      if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
