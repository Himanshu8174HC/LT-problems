class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        temp_sum = 0
        temp = 0
        seen = set()
        for i in range(len(nums)):
            while nums[i] in seen:
                seen.remove(nums[temp])
                temp_sum -=nums[temp]
                temp += 1
            seen.add(nums[i])
            temp_sum += nums[i]
            ans = max(ans, temp_sum)
        return ans
        
