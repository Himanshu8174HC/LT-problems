class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return ((n*(n+1))//2 - sum(nums))
    
    
    
    
    #######################
    
    se1 = set(list(range(len(nums))))
        res = list(se1-set(nums))
        if len(res)==1:
            return res[0]
        else:
            return len(nums)
