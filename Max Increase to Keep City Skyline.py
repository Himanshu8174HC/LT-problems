class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        row_max = []
        for i in (grid):
            row_max.append(max(i))
        
        
                
        for i in range(len(grid)):
            for j in range(i+1, len(grid)):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        
        col_max = []
        for i in (grid):
            col_max.append(max(i))
        
        
            
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                ans += min(row_max[i], col_max[j]) - grid[i][j]
                
        return ans
