class Solution:
    def isValid(self, s: str) -> bool:
        mapi = {
            
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []
        for i in s:
            if i not in mapi:
                if not stack or mapi[stack.pop()]!= i:
                    return False
                    print(stack)
            
            else:
                stack.append(i)
        return len(stack) == 0 
