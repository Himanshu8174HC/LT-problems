class Solution:
    def brokenCalc(self, s: int, t: int) -> int:
        
        ans = 0
        while s < t:
            ans += 1
            if t % 2:
                t += 1
            else:
                t //= 2
        return s - t + ans
