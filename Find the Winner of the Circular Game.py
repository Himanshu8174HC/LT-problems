class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ls = [i for i in range(1, n+1)]
        while len(ls) > 1:
            x = (k-1) % len(ls)
            ls.pop(x)
            ls = ls[x:] + ls[:x]
        return ls[0]
        
