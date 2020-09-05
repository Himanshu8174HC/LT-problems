class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans='0'
        for i in range(n):
            s=""
            for i in range(len(ans)):
                if(ans[i]=='1'):
                    s+='0'
                else:
                    s+='1'
            s=s[::-1]
            ans=ans+'1'+s
            
        return ans[k-1]
