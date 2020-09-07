class Solution:
    def reverse(self, x: int) -> int:
        if x>(2**31-1) or x<-(2**31):
            return 0
        if x<0:
            x=x*-1
            k=str(x)
            m=k[::-1]
            m=int(m)
            if m>(2**31-1) or m<-(2**31):
                return 0
            return m*-1
        else:
            k=str(x)
            m=k[::-1]
            m=int(m)
            if m>(2**31-1) or m<-(2**31):
                return 0
            return m
