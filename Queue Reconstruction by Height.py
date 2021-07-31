class Solution:
    def reconstructQueue(self, p: List[List[int]]) -> List[List[int]]:
        
        if len(p) <= 1:
            return p
        
        p = sorted(p, key=lambda x: (-x[0], x[1]))
        
        for i in range(len(p)):
            j = p[i][1]
            
            if j < i:
                temp = p.pop(i)
                p.insert(j, temp)
        return p
            
