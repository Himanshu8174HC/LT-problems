class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        temp = sorted(zip(efficiency, speed), reverse=True)
        t_heap = []
        ans = 0
        total = 0
        
        for effi, speed in temp:
            heappush(t_heap, speed)
            if len(t_heap) <= k:
                total += speed
            else:
                total += speed
                total -= heappop(t_heap)
            ans = max(ans, total*effi)
        return ans % 1000000007
                
