class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, d, parents):
            if not node:
                return
            if node.val == x:
                self.a = d
                self.a_parent = parents
            elif node.val == y:
                self.b = d
                self.b_parent = parents
            dfs(node.left, d+1, node)
            dfs(node.right, d+1,node)
        dfs(root, 0, None)
        return self.a == self.b and self.a_parent != self.b_parent
            
