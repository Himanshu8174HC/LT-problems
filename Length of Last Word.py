class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = " ".join(s.split())
        l=list(s.split(" "))
        if len(l)==0:
            return 0
        return len(l[-1])
