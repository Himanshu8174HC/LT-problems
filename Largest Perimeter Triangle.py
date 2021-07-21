class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        nums = sorted(nums , reverse = True)
        
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2] and nums[i+1] + nums[i+2] > nums[i] and nums[i+2] + nums[i] > nums[i+1]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
            
