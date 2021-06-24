class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        i = 0
        while i < len(s):
            temp = s[i:i+k][::-1]
            ans += (temp + s[i+k:i+2*k])
            i += 2*k
        return ans
