class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d = Counter(nums)
        while d[original] > 0:
            if d[original] > 0:
                original *= 2
            
        return original
        
