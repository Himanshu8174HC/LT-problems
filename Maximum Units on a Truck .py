class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        ans = 0
        for i in range(len(boxTypes)):
            
            
            if truckSize >= boxTypes[i][0] and truckSize > 0:
                ans += ((boxTypes[i][0]) * (boxTypes[i][1]))
                truckSize -= boxTypes[i][0]
                
            elif truckSize > 0:
                ans += (truckSize * (boxTypes[i][1]))
                truckSize -= boxTypes[i][0]
                
        return ans
