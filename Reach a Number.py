class Solution:
    def reachNumber(self, t: int) -> int:
        if t < 0:
            t = -t
        i = 2
        s = 1
        while (s < t or (s-t) % 2):
            s += i
            i+=1
        
        return i-1
