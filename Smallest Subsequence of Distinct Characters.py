class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d ={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        stack = []
        for ch in s:
            d[ch]-=1
            if ch in stack:
                continue
            while stack and stack[-1] > ch and d[stack[-1]]:
                stack.pop()
            stack.append(ch)
        return "".join(stack)
