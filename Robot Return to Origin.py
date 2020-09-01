class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start=0
        end=0
        for i in moves:
            if i=="R":
                start+=1
            elif i=="L":
                start-=1
            elif i=="D":
                end+=1
            elif i=="U":
                end-=1
        if start==0 and end==0:
            return True
        return False
                
