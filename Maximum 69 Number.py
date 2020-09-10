class Solution:
    def maximum69Number (self, num: int) -> int:
        k=list(str(num))
        for i in range(len(k)):
            if k[i]=="6":
                m=k[i]
                k[i]='9'
                l=''.join(k)
                return (int(l))

        return num
