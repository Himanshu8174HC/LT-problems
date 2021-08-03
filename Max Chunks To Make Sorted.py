class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        
        ans = 0
        for i in range(len(arr)):
            x = sorted(arr[:i+1])
            if x == [i for i in range(i+1)]:
                ans += 1
        return ans
                
