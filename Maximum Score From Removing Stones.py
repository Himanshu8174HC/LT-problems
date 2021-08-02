class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        temp = sorted([a,b,c])
        if temp[0] >= temp[2] - temp[1]:
            return (a + b + c) // 2
        return temp[0] + temp[1]
