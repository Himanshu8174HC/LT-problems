class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        temp = 0
        for i in root.children:
            temp = max(temp, self.maxDepth(i))
        return 1+temp
        
