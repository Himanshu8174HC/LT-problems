###########################################################################MORE EFFICIENT
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        ans =[]
        d1 ={}
        temp1 = A.split()
        ans =[]
        for i in temp1:
            if i in d1:
                d1[i] +=1
            else:
                d1[i] = 1
        
        d2 ={}
        temp2 = B.split()
        ans =[]
        for i in temp2:
            if i in d2:
                d2[i] +=1
            else:
                d2[i] = 1
                
        for i in temp1:
            if (i  not in temp2) and (d1.get(i) ==1):
                ans.append(i)
                
        for i in temp2:
            if (i not in temp1) and (d2.get(i) ==1):
                ans.append(i)
        return ans
        
#######################################################################LESS EFFICIENT
ans = []
        temp = A.split() + B.split()
        for i in temp:
            if temp.count(i) == 1:
                ans.append(i)
        return ans
                
            
        
