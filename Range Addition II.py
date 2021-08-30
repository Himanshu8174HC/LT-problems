class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
        row = m
        col = n
        
        for i in range(len(ops)):
            row = min(row, ops[i][0])
            col = min(col, ops[i][1])
        return row*col
        
        
