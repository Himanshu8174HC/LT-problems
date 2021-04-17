class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        def dfs(current, parent, grandparent):
            if not current:
                return 0
            nonlocal total
            if grandparent and grandparent.val %2 == 0:
                total += current.val
            
            dfs(current.left, current, parent)
            dfs(current.right, current, parent)
        dfs(root, None, None)
        
        return total
