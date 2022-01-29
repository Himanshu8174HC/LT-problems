class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        ans = len(nums)
        
        for i in range(len(nums)):
            if nums[i] == nums[0] or nums[i] == nums[-1]:
                ans -= 1
                
        return ans
   

############################################################O(N)
ans = 0
        Max_nums = max(nums)
        Min_nums = min(nums)
        
        for i in range(len(nums)):
            if Min_nums < nums[i] < Max_nums:
                ans += 1
        return ans
         
        
