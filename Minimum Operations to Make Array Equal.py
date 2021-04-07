class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return 1
        x = [i for i in range(n+1)]
        if n % 2 ==0:
            y = x[1::2]
        else:
            y = x[::2]
        return sum(y)
        
