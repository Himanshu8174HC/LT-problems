class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        temp = []
        def inorder(node):
            
            if not node:
                return []
            inorder(node.left)
            temp.append(node.val)
            inorder(node.right)
        inorder(root)
        
        
        d= {}
        for i in temp:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        if temp:
            maxi = max(d.values())
            return [k for k,v in d.items() if maxi==v]
        return temp
                
