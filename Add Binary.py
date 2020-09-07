class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        int_sum = int(a,2)+int(b,2)
        bin_sum = bin(int_sum)
        ans=str(bin_sum)
        return ans[2:]
