class Solution:
    def minCostToMoveChips(self, p: List[int]) -> int:
        
        odd = 0
        even = 0
        
        for i in p:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd > even:
            return even
        return odd
        
            
        
