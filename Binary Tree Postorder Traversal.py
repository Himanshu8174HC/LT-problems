class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        def help(node):
            if node:
                help(node.left)
                help(node.right)
                ans.append(node.val)
        help(root)
        return ans
