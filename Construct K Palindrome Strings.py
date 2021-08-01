class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if len(s) < k:
            return False
        d = Counter(s)
        
        temp = 0
        for i, v in d.items():
            if v % 2 != 0:
                temp += 1
                if temp > k:
                    return False
        return True
                
