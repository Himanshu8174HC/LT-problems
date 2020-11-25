class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            wor = "".join(sorted(word))
            if wor in d:
                d[wor].append(word)
            else:
                d[wor]=[word]
                
        ans = []
        for k, v in d.items():
            ans.append(v)
        return ans
