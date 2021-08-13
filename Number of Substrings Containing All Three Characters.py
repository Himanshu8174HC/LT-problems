class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        a = 0
        b = 0
        c = 0
        
        j = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] == "a":
                a += 1
            elif s[i] == "b":
                b += 1
            else:
                c += 1
            
            while a > 0 and b > 0 and c > 0:
                ans += len(s) - i
                if s[j] == "a":
                    a -= 1
                elif s[j] == "b":
                    b -= 1
                else:
                    c -= 1
                
                j += 1
        return ans
        
