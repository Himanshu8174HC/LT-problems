class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        ans = len(nums)
        
        for i in range(len(nums)):
            if nums[i] == nums[0] or nums[i] == nums[-1]:
                ans -= 1
                
        return ans
