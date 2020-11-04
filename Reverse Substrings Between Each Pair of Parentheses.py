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

    
############################################################### More Efficient

stack = []
reverse = []
        
        for i in range(len(s)):
            if s[i] == ')':  # pop the substring between nearest parentheses
                p = stack.pop()
                while p != '(':
                    reverse.append(p)
                    p = stack.pop()
                stack += reverse
                reverse = []
            else:
                stack.append(s[i])
        return ''.join(stack)
        
