class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                if i == j:
                    continue
                l = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                
                if l not in d:
                    d[l] = 1
                else:
                    d[l] +=1
               
            for key, value in d.items():
                ans = value *(value-1) + ans
        
        return ans
            
            
