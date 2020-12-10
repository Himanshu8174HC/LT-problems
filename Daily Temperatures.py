class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        temp = [0]*len(T)
        stack = []
        
        for i, v in enumerate(T):      
            while stack and v > T[stack[-1]]:
                j = stack.pop()
                temp[j] = i - j
            stack.append(i)
        
        return temp
        
