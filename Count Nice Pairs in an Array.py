class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        d ={}
        for i in nums:
            x = str(i)
            temp = i - int(x[::-1])
            if temp in d:
                d[temp] += 1
            else:
                d[temp] = 1
        
        count = 0
        for value in d.values():
            if value >1  :
                count += (value * (value -1))/2
        return int(count) % (10**9 +7)
        
