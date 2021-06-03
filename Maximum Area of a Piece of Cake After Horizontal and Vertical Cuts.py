class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        temp1 = [0] + horizontalCuts + [h]
        temp2 = [0] + verticalCuts + [w]
        temp1 = sorted(temp1)
        temp2 = sorted(temp2)
        
        height = 0
        for i in range(len(temp1)-1):
            x = temp1[i+1] - temp1[i]
            height = (max(height, x))
        width = 0
        for i in range(len(temp2)-1):
            x = temp2[i+1] - temp2[i]
            width = (max(width, x))
        return (height*width)%((10**9)+7)
        
