class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
      ans = 0
      for i in a:
        x = sum(i)
        ans = max(ans, x)
      return ans
