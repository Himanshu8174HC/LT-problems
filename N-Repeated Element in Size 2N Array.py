class Solution:
    def repeatedNTimes(self, A: List[int]) -> int: 
        d = {}
        for i in A:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        for key, value in d.items():
            if value >= len(A)//2:
                return key
###############################################################
count = [0]*10001
        
        for i in A:
            if count[i] == 1:
                return i
            count[i] += 1
################################################################
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int: 
        temp = set()
        for i in A:
            if i in temp:
                return i
            temp.add(i)
