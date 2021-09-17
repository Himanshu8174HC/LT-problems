class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = Counter(nums1)
        ans = []
        for i in nums2:
            if d[i] > 0:
                ans.append(i)
                d[i] -= 1
        return ans
                
        
