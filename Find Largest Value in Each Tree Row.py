class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        queue = [root]
        ans = []
        while queue:
            temp = []
            level_max = float("-inf")
            
            for node in queue:
                level_max = max(level_max, node.val)
                
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            ans.append(level_max)
            queue = temp
        return ans
            
        
        
