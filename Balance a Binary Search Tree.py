class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        temp = []
        def inorder(node):
            
            if not node:
                return []
            inorder(node.right)
            temp.append(node.val)
            inorder(node.left)
        inorder(root)
        
        temp = sorted(temp)
        
        def ans(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            n = TreeNode(temp[mid])
            n.left = ans(left, mid - 1)
            n.right = ans(mid + 1, right)

            return n

        return ans(0, len(temp) - 1)

        
