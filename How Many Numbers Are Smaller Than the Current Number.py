class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      num = sorted(nums)
      ans = []
      
      for i in nums:
        ans.append(num.index(i))
      return ans
        
