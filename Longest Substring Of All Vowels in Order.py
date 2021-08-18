class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        ans = 0
        
        j = 0
        seen = set(word[0])
        
        for i in range(1, len(word)):
            seen.add(word[i])
            
            if word[i] < word[i-1]:
                j = i
                seen = set(word[i])
            if len(seen) == 5:
                ans = max(ans, i-j +1)
        return ans
            
        
