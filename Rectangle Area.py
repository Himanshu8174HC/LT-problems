class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        a1=C-A
        a2=D-B
        ar1=a1*a2
        b1=G-E
        b2=H-F
        ar2=b1*b2
        ans=0
        a=max(A,E)
        b=max(B,F)
        c=min(C,G)
        d=min(D,H)
        if c>a and d>b:
            ans=(c-a)*(d-b)
        return ar1+ar2-ans
