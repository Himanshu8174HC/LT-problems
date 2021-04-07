class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        ans = 0
        
        for i in range(len(s)):
            if i <= (len(s)//2)-1:
                if s[i] in "aeiouAEIOU":
                    ans +=1
            else:
                if s[i] in "aeiouAEIOU":
                     ans-=1
                
        
        if ans:
            return False
        return True
            
