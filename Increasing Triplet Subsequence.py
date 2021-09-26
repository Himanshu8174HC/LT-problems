class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m1 = float("inf")
        m2 = float("inf")
        for i in nums:
            if i < m1:
                m1 = i
            elif i < m2 and i > m1:
                m2 = i
            elif i > m2:
                return True
        return False
        
