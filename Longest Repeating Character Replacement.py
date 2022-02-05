class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        
        i = 0
        j = 0
        ans = 0
        temp = 0
        temp2 = 0
        
        while j < len(s):
            d[s[j]] += 1
            temp += 1
            temp2 = max(temp2, d[s[j]])
            while temp - temp2 > k:
                d[s[i]] -= 1
                i += 1
                temp -= 1
                
            ans = max(ans, j - i + 1)
            j += 1
        
        return ans
