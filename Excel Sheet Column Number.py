class Solution:
    def titleToNumber(self, s: str) -> int:
r = 0
        
        for i in range(len(s)):
            r += (ord(s[len(s) - i - 1]) - 64)*26**i
            
        return r
        
        
 #################################################
 class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for char in s:
            x = ord(char) - ord('A') + 1
            res = res * 26 + x
        return res
