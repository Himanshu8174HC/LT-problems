class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)

        inOrder(root)
        return min(abs(res[i+1]-res[i]) for i in range(len(res)-1))
            
            
