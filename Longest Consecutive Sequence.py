class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in s:
                temp = 1
                while num+1 in s:
                    temp += 1
                    num += 1
                ans = max(ans, temp)
   
        return ans
