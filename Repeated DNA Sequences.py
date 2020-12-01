class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s)- 9):
            if s[i:i+10] in d:
                d[s[i:i+10]] += 1
            else:
                d[s[i:i+10]] = 1
        ans = []     
        for i in d.keys():
            if d[i] >1:
                ans.append(i)
        return ans
