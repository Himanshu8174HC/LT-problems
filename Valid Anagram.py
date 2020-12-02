class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in t:
            if i in d:
                d[i] -= 1
            else:
                return False

        for value in d.values():
            if value != 0:
                return False
        
        return True
        
        
#################################################### Using sort
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) ==sorted(list(t))
