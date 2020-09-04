class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m1,m2=0,0
        for i in nums:
            if i==1:
                m1+=1
                if m1>m2:
                    m2=m1
            else:
                m1=0
        return m2
            
