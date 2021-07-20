class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        
        rungs = [0] + rungs
        ans = 0
        for i in range(len(rungs)-1):
            if rungs[i+1] - rungs[i] > dist:
                ans += ((rungs[i+1] - rungs[i] - 1)//dist)
                
                    
            
        return ans
