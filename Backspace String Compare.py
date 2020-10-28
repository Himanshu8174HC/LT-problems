class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s =[]
        t =[]
        for i in S:
            if i.isalpha():
                s.append(i)
            elif i =="#" and len(s)>0:
                s.pop()
        for i in T:
            if i.isalpha():
                t.append(i)
            elif i =="#" and len(t)>0:
                t.pop()
        return s == t
        
