class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        num = []
        temp = [root]
        while temp:
            t = temp.pop()
            num.append(t.val)
            if t.left:
                temp.append(t.left)
            if t.right:
                temp.append(t.right)
        
        if len(set(num)) == 1:
            return -1
        return sorted(set(num))[1]
                
