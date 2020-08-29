class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m=max(arr)+k
        l=list(range(1,m+1))
        for i in arr:
            if i in l:
                l.remove(i)
        
        return l[k-1]
