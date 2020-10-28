class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        count = 0
        stack = []
        flag = 0
        for i in range(len(S)):
            if S[i] == "(":
                flag = 1
                stack.append("(")
            if S[i] == ")":
                if flag == 1:
                    count += 2**(len(stack)-1)
                    flag = 0                
                stack.pop()
        return count 
    
    
    ################################################################More efficient
    class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0] 

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
