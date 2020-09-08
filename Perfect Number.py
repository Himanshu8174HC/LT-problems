class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        if num<0:
            return False
        count=1
        n=int(sqrt(num))
        for i in range(2,n+1):
            if num%i==0:
                k=num//i
                count=count+i+k
        return count==num
