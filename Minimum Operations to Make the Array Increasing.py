class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        temp = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            if temp[-1] >= nums[i]:
                temp.append(temp[-1]+1)
                ans += abs(temp[-1] - nums[i])
            else:
                temp.append(nums[i])
        return ans
