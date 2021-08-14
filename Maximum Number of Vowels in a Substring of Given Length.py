class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        
        j = 0
        d = {'a':0,'e':0,'i':0,'o':0,'u':0}
        ans = 0
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            
            if i-j+1==k:
                ans = max(ans,sum(d.values()))
                if s[j] in d:
                    d[s[j]] -= 1
                j+=1
        return ans
