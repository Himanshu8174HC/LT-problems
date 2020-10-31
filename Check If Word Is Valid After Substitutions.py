class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == 'c':
                if len(stack) < 2 or stack.pop() != 'b' or stack.pop() != 'a':
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0 
