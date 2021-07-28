class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = {}
        for i, c in enumerate(s):
            d[c] = i
        
        rightMost = -1
        leftMost = -1
        ans = []
        
        for i, c in enumerate(s):
            rightMost = max(rightMost, d[c])
            
            if i == rightMost:
                ans.append(rightMost - leftMost)
                
                leftMost = i
        return ans
            
        
