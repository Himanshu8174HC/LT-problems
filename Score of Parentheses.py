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
