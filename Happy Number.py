class Solution:
    def isHappy(self, n: int) -> bool:
        temp = [int(i) for i in str(n)]
        s = set()
        while sum(temp)!=1:
            SUM = 0
            for i in temp:
                SUM += i**2
            if SUM in s:
                return False
            else:
                s.add(SUM)
                temp = [int(i) for i in str(SUM)]
                
        return True

        
