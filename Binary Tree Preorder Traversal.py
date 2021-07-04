class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        return []
