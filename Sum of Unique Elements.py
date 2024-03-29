class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
      d = {}
      for i in nums:
        if i in d:
          d[i] += 1
        else:
          d[i] = 1
      
      ans = 0
      for k, v in d.items():
        if v == 1:
          ans += k
      return ans
        
