class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        g={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        def str_to_int(num,k,r):
            for i in range(len(num)-1,-1,-1):
                r+=g[num[i]]*k
                k*=10
            return(r)
        return str(str_to_int(num1,1,0)+str_to_int(num2,1,0))
        
        
 ####################################################################
 class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1, i2 = 0, 0
        d1, d2 = 10**(len(num1)-1), 10**(len(num2)-1)

        for i in num1:
            i1 += (ord(i) - ord("0")) * d1
            d1 //= 10

        for i in num2:
            i2 += (ord(i) - ord("0")) * d2
            d2 //= 10


        return str(i1 + i2)
