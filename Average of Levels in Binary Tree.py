class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ans, queue = [], [root]
        sumation  = 0
        while queue:
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                sumation = sumation+node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sumation/len(queue))
            sumation = 0
        return ans
                
        
        
        
        
        
