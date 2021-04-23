class Solution:
    def countBinarySubstrings(self, s: str) -> int:
      if not s:
        return 0
      temp = s[0]
      curr = 0
      pre = 0
      
      ans = 0
      for i in s:
        if i == temp:
          curr += 1
          
        else:
          ans += min(curr, pre)
          pre = curr
          curr = 1
          temp = i
          
          
          
      ans += min(curr, pre)
      return ans
