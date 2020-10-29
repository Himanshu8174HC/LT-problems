class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        a = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[a]:
                a += 1
                stack.pop()
        return len(stack) == 0  
