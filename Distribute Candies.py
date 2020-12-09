########################################################################## DICTIONARY SOLUTION
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a = len(candyType)//2
        d = {}
        for i in candyType:
            if i not in d:
                d[i] = 1
            else:
                continue
        count = 0       
        for value in d.values():
            count += value
            
        if count > a:
            return a
        else:
            return count
                
                
###################################################################SET Solution
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        if len(set(candyType)) > len(candyType)//2:
            return len(candyType)//2
        else:
            return len(set(candyType))
                
