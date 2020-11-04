class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i , ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch ==")":
                index = stack.pop(-1)
                s = s[:index+1] + s[index+1:i][::-1] +s[i:]
        
        s=s.replace('(','')
        s=s.replace(')' , '')
        return s
        
