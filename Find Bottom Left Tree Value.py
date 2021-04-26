class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
      levels = [root]
      ans = 0
      while levels:
          nxt = []
          for node in levels:
              if node.left:
                  nxt.append(node.left)
              if node.right:
                  nxt.append(node.right)
          if not nxt:
              ans = levels[0].val
              break
          levels = nxt
      return ans
        
