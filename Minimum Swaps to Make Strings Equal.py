class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        count_x = 0
        count_y = 0
        
        for i in range(len(s1)):
            if s1[i] != s2[i] and s1[i] == "x":
                count_x += 1
            elif s1[i] != s2[i] and s1[i] == "y":
                count_y += 1
        
        if count_x % 2  != count_y % 2:
            return -1
        return count_x // 2 + count_x % 2 + count_y // 2 + count_y % 2
        
        
            
