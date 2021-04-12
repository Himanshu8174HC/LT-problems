class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans = [0]*2
        
        def Dfs(node,level):
            if not node:
                return 
            
            if level == ans[0]:
                ans[1]+=node.val
            elif level > ans[0]:
                ans[0] = level
                ans[1] = node.val
                
            Dfs(node.left, level+1)
            Dfs(node.right, level+1)
            
        Dfs(root, 0)
        return ans[1]
            
