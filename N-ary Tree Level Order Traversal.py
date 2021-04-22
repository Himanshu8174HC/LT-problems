class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
      if not root:
        return []
      ans = []
      queue = [root]
      while queue:
        temp1 = []
        temp2 = []
        for node in queue:
          temp1.append(node.val)
          if node.children:
            temp2 += [child for child in node.children]
                    
        ans.append(temp1)
        queue = temp2
      return ans
          
        
            
            
        
      
        
          
        
