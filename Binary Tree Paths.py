class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def recur(root, temp, ans):
            if not root:
                return
            if len(temp) == 0:
                temp += str(root.val)
            else:
                temp += "->" +str(root.val)
            
            if not root.right and not root.left:
                ans.append(temp)
                return
            
            recur(root.left, temp, ans)
            recur(root.right, temp, ans)
            

        ans  = []
        temp = ""
        recur(root, temp, ans)
        return ans
        
