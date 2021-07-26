class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        
        temp = []
        
        for i in range(len(nums)//2):
            temp.append(nums[i]+nums[(len(nums)-1) - i])
        
        return max(temp)
        
