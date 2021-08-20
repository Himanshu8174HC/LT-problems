class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        ans = 0
        j = 0
        pro = 1
        
        for i in range(len(nums)):
            pro *= nums[i]
            
            while pro >= k and i >= j:
                pro /= nums[j]
                j += 1
            
            ans += i - j +1
        return ans
        
