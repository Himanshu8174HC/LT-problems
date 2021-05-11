class Solution:
    def maxScore(self, CP: List[int], k: int) -> int:
      ans = total = sum(CP[:k])
      for i in range(k-1, -1, -1):
        total += CP[i + (len(CP)-k)]
        total -= CP[i]
        ans = max(total, ans)
      return ans
      
