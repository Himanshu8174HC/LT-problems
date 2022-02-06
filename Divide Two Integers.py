class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        temp = abs(dividend)
        temp1 = abs(divisor)
        
        ans = 0
        while temp >= temp1:
            temp2 = temp1
            Q = 1
            
            while temp >= temp2:
                temp -= temp2
                ans += Q
                Q += Q
                temp2 += temp2
        
        if (dividend < 0 and divisor >= 0)  or (dividend >= 0 and divisor < 0) :
            ans = -ans
        return min(2147483647, max(-2147483648, ans))
        
