class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        ans = []
        
        
        
        def help(node,temp):
            if not node:
                return ans
            
            
            
            if not node.right and not node.left:
                if sum(temp +[node.val]) == targetSum:
                    ans.append(temp+[node.val])
            
            help(node.left, temp+[node.val])
            help(node.right, temp+[node.val])
                
            
                
                
                
        help(root, [])
        return ans
                
            
        
