class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            tem=timePoints[i].split(':')
            timePoints[i]=int(tem[0])*60+int(tem[1])
        diff=float('inf')
        timePoints=sorted(timePoints)
        for i in range(1,len(timePoints)):
            temp=timePoints[i]-timePoints[i-1]
            diff=min(diff,temp)
            diff=min(diff,24*60-timePoints[-1]+timePoints[0])
        return diff
