class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        ans = []
        
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                lo = i+1
                hi = len(nums)-1
                add = - nums[i]
                
                while lo < hi :
                    if nums[lo] + nums[hi] == add:
                        temp = []
                        temp.append(nums[i])
                        temp.append(nums[lo])
                        temp.append(nums[hi])
                        ans.append(temp)
                        
                        while lo < hi and nums[lo] == nums[lo+1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi-1]:
                            hi -= 1
                            
                        lo += 1
                        hi -= 1
                    elif nums[lo] + nums[hi] < add:
                        lo += 1
                    else:
                        hi -= 1
        return ans
