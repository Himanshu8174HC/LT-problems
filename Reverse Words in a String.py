class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
        
        
        
 #########################
 class Solution:
    def reverseWords(self, s: str) -> str:
        r = " ".join(s.split())
        l=list(r.split(" "))
        l=l[::-1]
        ans= " ".join(l)
        return ans
