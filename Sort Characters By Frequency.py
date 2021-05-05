class Solution:
    def frequencySort(self, s: str) -> str:
      d = {}
      for i in s:
        if i in d:
          d[i] += 1
        else:
          d[i] = 1
          
      d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
      ans = ''
      for k, v in d.items():
        ans += k*v
      return ans[::-1]
