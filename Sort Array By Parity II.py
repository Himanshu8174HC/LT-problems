class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans=[0]*len(A)
        j=0
        k=1
        for i in A:
            if i%2==0:
                ans[j]=i
                j+=2
            else:
                ans[k]=i
                k+=2
        return ans
