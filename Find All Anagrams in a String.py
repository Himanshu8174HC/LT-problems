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
