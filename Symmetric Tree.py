class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return root1.val == root2.val and dfs(root1.right, root2.left) and dfs(root1.left, root2.right)
        return dfs(root, root)
