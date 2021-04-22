class Solution:
    def goodNodes(self, root: TreeNode, m = float('-inf')) -> int:
      if not root:
        return 0
      
      if root.val >= m:
        return 1+ self.goodNodes(root.right, root.val) + self.goodNodes(root.left, root.val)
      else:
        return self.goodNodes(root.right, m) + self.goodNodes(root.left, m)
