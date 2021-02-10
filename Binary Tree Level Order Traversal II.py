class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, queue = [], [root]
        temp = []
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
            temp = []
        return ans[::-1]
                
