class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        tw = 0
        on = 0
        
        for i in nums:
            multi = 0
            
            while i:
                if i % 2 != 0:
                    on += 1
                    i -= 1
                else:
                    i //= 2
                    multi += 1
            tw = max(tw, multi)
        return tw + on
