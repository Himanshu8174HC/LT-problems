class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        
        def help(node):
            if node:
                help(node.left)
                ans.append(node.val)
                help(node.right)
            return []
        help(root1)
        help(root2)
        return sorted(ans)
        
