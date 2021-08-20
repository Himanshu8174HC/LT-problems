class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = defaultdict(int)
        ans = 0
        count = 0
        j = 0
        
        for i in range(len(s)):
            
            d[s[i]] += 1
            count += 1
            
            if d[s[i]] > 1:
                
                while d[s[i]] > 1 and j <= i:
                    d[s[j]] -= 1
                    count -= 1
                    j += 1
            ans = max(ans, count)
                    
        return ans
                
