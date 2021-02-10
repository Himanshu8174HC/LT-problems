class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            queue = [root]
            leaf = []
            while queue:
                node = queue.pop()
                if not node.left and not node.right:
                    leaf.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return leaf
        return dfs(root1) == dfs(root2)
                    
            
