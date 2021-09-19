class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            
        
        temp = [str(i) for i in nums]
        
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                if int(temp[i]+temp[j]) > int(temp[j]+temp[i]):
                    temp[i], temp[j] = temp[j], temp[i]
        temp = temp[::-1]
        ans =  int("".join(temp))
        return str(ans)
        
                    
