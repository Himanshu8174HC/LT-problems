class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        h, token = len(s) // 2, ''
        
        for i in range(h):
            token += s[i]
            multiplier = len(s) // len(token)
            if token * multiplier == s: return True
            
        return False
