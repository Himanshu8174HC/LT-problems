class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if len(nums) <= 4:
            return sum(nums) / k
        
        sum_k = float("-inf")
        temp = 0
        i = 0
        for j in range(len(nums)):
            temp += nums[j]
            if j - i +1 == k:
                temp2 = temp / k
                sum_k = max(sum_k, temp2)
                temp -= nums[i]
                i += 1
        return sum_k
            
