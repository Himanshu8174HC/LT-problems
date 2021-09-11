class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points = sorted(points, key = lambda x: x[0])
        ans = float("-inf")
        
        for i in range(len(points)-1):
            if (points[i+1][0] - points[i][0]) > ans:
                ans = (points[i+1][0] - points[i][0])
            
        return ans
        
