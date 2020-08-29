class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        n=len(nums)
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v > n/3:
                l.append(k)
        return l
