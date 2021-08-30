class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        reach = 0
        i = 0
        ans = 0
        
        while reach < n:
            if  i >= len(nums):
                reach += reach+1
                ans += 1
            elif nums[i] <= (reach + 1) and i < len(nums):
                reach += nums[i]
                i += 1
            else:
                reach += reach+1
                ans += 1
        return ans
                 
