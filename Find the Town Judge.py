class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        temp = [0] * (n+1)
        for i, j in trust:
            temp[i] -=1
            temp[j] += 1
        
        for i in range(1, n+1):
            if temp[i] == n-1:
                return i
        return -1
