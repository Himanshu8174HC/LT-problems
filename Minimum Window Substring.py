class Solution:
    def minWindow(self, s: str, t: str) -> str:    
        
        d = Counter(t)
        ans = ""
        mini = 10**6
        j = 0
        count = len(d)
        
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    count -= 1
            
            while count == 0 and j <=i :
                if i-j +1 < mini:
                    mini = i-j+1
                    ans = s[j:i+1]
                if s[j] in d:
                    d[s[j]] += 1
                    if d[s[j]] == 1:
                        count += 1
                j += 1
                            
        return ans
