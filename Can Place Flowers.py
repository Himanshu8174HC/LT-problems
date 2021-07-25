class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        
        f = [0] + f + [0]
        
        
        for i in range(1, len(f)-1):
            if f[i] == 0 and f[i-1] != 1 and f[i+1] != 1:
                n -= 1
                f[i] = 1
                
        return n <= 0
                
        
        
        
        
