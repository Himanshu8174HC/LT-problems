class Solution:
    def maxPower(self, s: str) -> int:
        ans = [1]
        ls = list(s)
        count = 1
        for i in range(0,len(ls)-1):
            if(ls[i] == ls[i+1]):
                count+=1
                ans.append(count)
            else:
                count=1
        return(max(ans))
