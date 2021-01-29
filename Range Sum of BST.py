class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                return dfs(node.left) + dfs(node.right) + node.val
        return dfs(root)
