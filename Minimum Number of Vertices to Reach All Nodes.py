class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        
        for x,y in edges:
            if y in ans:
                ans.remove(y)
        return list(ans)
        
