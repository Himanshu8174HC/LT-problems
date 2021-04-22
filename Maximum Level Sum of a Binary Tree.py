class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
      if not root:
        return 0
      
      level = 0
      queue = [root]
      summ = float("-inf")
      
      while queue:
        temp = []
        curr = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            temp.append(node.val)
            
            if node.left:
              curr.append(node.left)
            if node.right:
              curr.append(node.right)
        level += 1
        count = sum(temp)
        if count > summ:
          summ = count
          pos = level
        queue = curr
        
      return pos
          
            
      
        
        
        
      
      
      
      
        
