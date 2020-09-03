class Solution:
    def maxScore(self, s: str) -> int:
        if s=="0"*len(s):
            return len(s)-1
        if s=="1"*len(s):
            return len(s)-1
        l=[]
        for i in range(1,len(s)):
            k=s[:i]
            ls=s[i:]
            
            ans= k.count("0")+ls.count("1")
            l.append(ans)
        return max(l)
