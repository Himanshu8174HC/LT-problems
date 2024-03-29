class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root:
          root.right = self.removeLeafNodes(root.right, target)
          root.left = self.removeLeafNodes(root.left, target)
          if not root.right and not root.left and root.val == target:
            return None
        return root
