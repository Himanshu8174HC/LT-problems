class Solution:
    def minDeletions(self, s: str) -> int:
        
        temp = Counter(s)
        uni = set()
        
        ans = 0
        for i, v in temp.items():
            
            while v > 0 and v in uni:
                ans += 1
                v -= 1
            uni.add(v)
        return ans
            
        
