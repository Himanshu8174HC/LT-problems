class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        di_s = {}
        di_t = {}
        
        for i in range(len(s)):
            
            
            le_s = s[i]
            if le_s not in di_s:
                di_s[le_s] = i
                
                
            le_t = t[i]
            if le_t not in di_t:
                di_t[le_t] = i
                
                
            if di_s[le_s] != di_t[le_t]:
                return False
            
        return True
                
            
                


        
        
            
                
        
