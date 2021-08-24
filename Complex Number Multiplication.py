class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        num1_r, num1_i = num1.split('+')
        num2_r, num2_i = num2.split('+')
        
        num1_i = num1_i[:-1]
        num2_i = num2_i[:-1]
        
        real = int(num1_r)*int(num2_r)-int(num1_i)*int(num2_i)
        imag = int(num1_r)*int(num2_i)+int(num1_i)*int(num2_r)
        
        return str(real)+'+'+str(imag)+'i'
        
        
