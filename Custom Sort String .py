class Solution:
    def customSortString(self, order: str, str: str) -> str:
        ans = ""
        
        for i in order:
            if i in str:
                ans += i * str.count(i)
                str = str.replace(i, '')
        ans += str
        return ans
        
