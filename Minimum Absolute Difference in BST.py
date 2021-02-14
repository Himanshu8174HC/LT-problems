class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        temp = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            temp.append(node.val)
            inorder(node.right)
        inorder(root)
        min_diff = temp[1] - temp[0]
        for i in range(1, len(temp)):
            diff = temp[i] - temp[i-1]
            min_diff = min(min_diff, diff)
        return min_diff
        
        
