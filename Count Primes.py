class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        temp = [1]*n
        temp[0] = 0
        temp[1] = 0
        for i in range(2, int(n**0.5)+1):
            if temp[i] == 1:
                for j in range(i*i, n,i):
                    temp[j]= 0
        return sum(temp)
        
