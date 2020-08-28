class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=nums[0:len(nums):2]
        return sum(l)
