class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w = s.split()
        if len(w) != len(pattern):
            return False
        
        d = {}
        for p, w in zip(pattern, w):
            if p in d:
                if d[p] != w:
                    return False
                
            elif w in d.values():
                return False
            
            else:
                d[p] =w
                
        return True
        
       
