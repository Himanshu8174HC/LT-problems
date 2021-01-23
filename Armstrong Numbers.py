class Solution:
    def armstrongNumber (ob, n):
        # code here 
        s = str(n)
        ans = 0
        for i in s:
            ans += int(i)*int(i)*int(i)
        if int(ans) == n:
            return "Yes"
        return "No"
             
