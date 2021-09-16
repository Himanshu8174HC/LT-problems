class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        add = 0
        ans = 0
        d = {0:-1}
        
        for i in range(len(nums)):
            if nums[i] == 1:
                add += 1
            else:
                add -= 1
            
            if add in d:
                ans = max(ans, i-d[add])
            else:
                d[add] = i
        return ans
