class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            i = 1
            while i < len(n) and x >= int(n[i]):
                i += 1
        else:
            i = 0
            while i < len(n) and x <= int(n[i]):
                i += 1
        ans = n[:i] + str(x) + n[i:]
        return ans
