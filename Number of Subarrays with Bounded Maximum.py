class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        s = -1
        e = -1
        ans = 0
        
        for i, n in enumerate(nums):
            if left <= n <= right:
                e = i
                
            if right < n:
                s = i
                e = i
                
            ans += (e-s)
            
        return ans
        
