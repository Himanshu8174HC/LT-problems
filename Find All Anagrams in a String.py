##########################################################################More Efficient
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)==0 or len(p) == 0 or len(s)<len(p):
            return []
        if s == p:
            return [0]
        ans = []
        d1 = {}
      
        for i in p:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
                
        d2 = {}
        
        for i in range(len(p)):
            if s[i] in d2:
                d2[s[i]] +=1
            else:
                d2[s[i]] = 1
                
        if d1 == d2:
            ans.append(0)
            
        for i in range(1,(len(s)-len(p)+1)):
            d2[s[i-1]] -= 1
            if d2[s[i-1]] == 0:
                del d2[s[i-1]]
                
            
            temp = i+len(p)-1
            if s[temp] in d2:
                d2[s[temp]] +=1
            else:
                d2[s[temp]] = 1
            
            if d1 == d2:
                ans.append(i)
                
        return ans

    
########################################################Less Efficient





class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        t = "".join(sorted(p))
        temp = ''
        
        ans = []
        start = 0
        
        for c in s:
            temp += c
            if len(temp)== len(t):
                if "".join(sorted(temp)) == t:
                    ans.append(start)
                temp = temp[1:]
                start +=1
                
        return ans
