class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result1=0
        result2=0
        
        for char1 in num1:
            result1=10*result1+num[char1]
        for char2 in num2:
            result2=10*result2+num[char2]
            
        return str(result1*result2)
