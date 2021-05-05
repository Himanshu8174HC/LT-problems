class Solution:
    def canJump(self, nums: List[int]) -> bool:
      temp = 0
      for i in range(len(nums)):
        temp = max(nums[i], temp)
        if temp == 0 and i != len(nums) - 1:
          return False
        temp -= 1
      return True
        
