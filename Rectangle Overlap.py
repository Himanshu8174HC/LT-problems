class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ans = 0
        A=max(rec1[0],rec2[0])
        B=max(rec1[1],rec2[1])
        C=min(rec1[2],rec2[2])
        D=min(rec1[3],rec2[3])
        if C>A and D>B:
            ans=(C-A)*(D-B)
        if ans==0:
            return False
        return True 
