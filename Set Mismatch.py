#######################################LESS EFICIENT
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        ans =[]
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i] =1
                
        for key, value in d.items():
            if value>1:
                ans.append(key)
        for i in range(1, len(nums)+1):
            if i not in nums:
                ans.append(i)
                
        return ans
        
######################################################### MORE EFFICIENT
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if len(nums) ==0:
            return nums
        set_sum = sum(set(nums))
        return [sum(nums) - set_sum, sum(range(1, len(nums) + 1)) - set_sum]
