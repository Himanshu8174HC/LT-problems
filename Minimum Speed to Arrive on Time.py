class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        if len(dist) - 1 >= hour:
            return -1
        
        left = 1
        right = 10**7 + 1
        while left < right:
            mid = (left + right) // 2
            t = sum(math.ceil(i/mid) for i in dist[:-1]) + dist[-1]/mid
            
            if t > hour:
                left = mid + 1
            else:
                right = mid
        return left
                    
            
        
            
            
        
