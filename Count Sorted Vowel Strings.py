class Solution:
    def countVowelStrings(self, r: int) -> int:
        
       # (n+r-1)!//(n-1!)*(r!)
       # n = 5 {a,e,i,o,u}
        
        num = math.factorial(5+r-1) 
        t1 = 24    #(n-1)!                    
        t2 = math.factorial(r)
        t = t1*t2
        
        return num//t
