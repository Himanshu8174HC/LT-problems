class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        n = len(s)
        for i in range(n-2, -1, -1):
             shifts[i] += shifts[i+1]
    
        ans = ""
        for i in range(n):
            x = ord(s[i])
            y = shifts[i]
            temp = (x + y - ord('a'))%26
            ans += chr(temp + ord('a'))
        return ans
            
                
            
            
        
            
            
            
        
            
        
