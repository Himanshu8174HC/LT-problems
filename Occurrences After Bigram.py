class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        temp = text.split()
        print(temp)
        ans = []
        for i in range(len(temp) - 2):
            if temp[i] == first and temp[i+1] == second:
                ans.append(temp[i+2])
        return ans
                
        
