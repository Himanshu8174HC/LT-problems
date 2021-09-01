class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        max_len = 0
        
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            length = 0    
            while nums[i] != -1:
                nums[i], i = -1, nums[i]
                length += 1
            if length > max_len:
                max_len = length
                    
        return max_len
        
            
        
