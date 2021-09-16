class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = 0
        down  = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        ans= []
        direction = 0
        while top <= down and left <= right:
            if direction == 0:
                for i in range(left, right+1):
                    ans.append(matrix[top][i])
                    
                top += 1
            
            elif direction == 1:
                for i in range(top, down+1):
                    ans.append(matrix[i][right])
                right -= 1
            
            elif direction == 2:
                for i in reversed(range(left, right+1)):
                    ans.append(matrix[down][i])
                down -= 1
            
            elif direction == 3:
                for i in reversed(range(top, down+1)):
                    ans.append(matrix[i][left])
                    
                left += 1
            direction = (direction + 1) % 4
        return ans
                    
                    
        
