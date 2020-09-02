class Solution:
    def countSegments(self, s: str) -> int:
        s = " ".join(s.split())
        if len(s)==0:
            return 0
        
        l=list(s.split(" "))
        return len(l) 
