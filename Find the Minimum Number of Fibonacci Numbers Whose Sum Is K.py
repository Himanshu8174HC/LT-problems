class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        Fibo = [1,1]
        for i in range(k):
            if Fibo[-1] > k:
                break
            Fibo.append(Fibo[-1]+Fibo[-2])
        
        
        Fibo = sorted(Fibo, reverse = True)
        print(Fibo)
        ans = 0
        for i in Fibo:
            if k in Fibo:
                return 1
            elif i <k and k>0:
                ans += 1
                k -= i
                if k in Fibo:
                    return ans+1
            
                
                
        
        
 ####################################################################################
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        a,b,res = 1,1,0
        while b < k:
            a,b = b,a+b
        while b > 0:
            if b <= k:
                res += 1
                k -= b
            a,b = b-a,a
        return res
