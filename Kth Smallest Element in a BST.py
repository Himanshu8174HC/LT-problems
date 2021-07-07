class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        temp = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if len(temp) == k:
                return 
            temp.append(node.val)
            inorder(node.right)
            
        inorder(root)
        return temp[-1]
            
        
