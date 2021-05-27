class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        
        temp = []
        for i in words:
            temp.append(set(i))
        
        for i in range(1, len(words)):
            for j in range(i):
                if not temp[i].intersection(temp[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
                    
        return ans
            
