class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1 , "V":5 , "X":10, "L":50, "C":100, "D":500, "M":1000}
        n=len(s)
        counter=d.get(s[-1])
        for k in range(n-1,0,-1):
            if d[s[k]]<=d[s[k-1]]:
                counter+=d[s[k-1]]
            else:
                counter-=d[s[k-1]]
        return counter
                
