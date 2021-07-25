class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        temp = s[::-1]
        if temp == s:
            return True
        else:
            for i, j in enumerate(s):
                if temp[i] != j:
                    temp = temp[0:i] + temp[i+1:]
                
                    if temp == temp[::-1]:
                        return  True
                
                    s = s[0:i] + s[i+1:]
                    return s == s[::-1]
                   
            
        
                
                
