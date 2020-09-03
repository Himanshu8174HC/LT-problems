class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        i=1
        while i<len(points) :
            if points[i][0]<=points[i-1][1] :
                points.pop(i)
            else :
                i+=1
        return len(points)
