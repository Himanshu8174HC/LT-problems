class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums) <= 4:
            return 0
        
        max_i = [float("-inf")]*4
        min_i = [float("+inf")]*4
        
        for k in nums:
            if k > max_i[0]:
                max_i[0] = k
                for i in range(0,3):
                    if max_i[i] > max_i[i+1]:
                        max_i[i], max_i[i+1] = max_i[i+1], max_i[i]
            if k < min_i[0]:
                min_i[0] = k
                for i in range(0,3):
                    if min_i[i] < min_i[i+1]:
                        min_i[i], min_i[i+1] = min_i[i+1], min_i[i]
                        
        return min(max_i[i] - min_i[3 - i] for i in range(4))
                        
