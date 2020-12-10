class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        ans = 0
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] =1
        print(d)       
        for i in d:
            if i+1 in d.keys():
                ans = max(ans, d[i]+d[i+1])
                print(ans)
        return ans
                
