#########################################################More efficient
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []
        for i in nums2:
            while stack and i>stack[-1]:
                d[stack.pop()] = i
            stack.append(i)
        return [d.get(num,-1) for num in nums1]
                
#######################################################Less eficient
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            n2 = nums2.index(i)
            for j in range(n2,len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    break
            else:
                res.append(-1)
                
        return res
        
