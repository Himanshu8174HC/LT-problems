class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            
            if first != second:
                heapq.heappush(stones, -abs(first - second))
                
        if len(stones):
            return abs(stones[0]) 
        else:
            return 0
            
            
        
        
