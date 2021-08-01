class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        k -= n
        temp = "-bcdefghijklmnopqrstuvwxy-"
        
        ans = "z" * (k // 25)
        if k % 25:
            ans = temp[k % 25] + ans
        ans = "a"*(n - len(ans)) + ans
        return ans
            
