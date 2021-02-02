class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        res = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)

        inOrder(root)
        tree = TreeNode()
        temp = tree
        for i in res:
            
            temp.right = TreeNode(i)
            
            temp = temp.right
        return tree.right
