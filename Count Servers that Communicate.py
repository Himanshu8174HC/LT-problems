class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        ans = 0
        points = []
        count_row = [0]*len(grid)
        count_col = [0]*len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    points.append((i,j))
                    count_row[i] += 1
                    count_col[j] += 1
        
        for i,j in points:
            if count_row[i] >1 or count_col[j] >1:
                ans += 1
        return ans
                    
