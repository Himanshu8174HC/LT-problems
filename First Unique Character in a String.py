class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)        
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
            
        return -1
        
        
        
############################################################ANother solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, v in enumerate(s):
            if v not in dic:
                dic[v] = i
            elif v in dic:
                dic[v] = "rep"
        
        for d in dic:
            if dic[d] != "rep":
                return dic[d]
        return -1
