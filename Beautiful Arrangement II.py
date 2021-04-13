class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [x for x in range(1, n+1)]
        for x in range(k-1):
            ans = ans[:x+1] + ans[x+1:][::-1]
        return ans

            
