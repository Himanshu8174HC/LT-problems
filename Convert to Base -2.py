class Solution:
    def baseNeg2(self, N: int) -> str:
        if N in [0, 1]:
            return str(N)
        if N % 2 == 0:
            return self.baseNeg2(N // -2) + '0'
        else:
            return self.baseNeg2((N - 1) // -2) + '1'
            
            
            
 ############Explanation
Each time we decompose a number using N = 2 * q + r, it's like doing bin(N) = bin(q) + str(r)
Reversely (from the bottom-up perspective), 1 is 0b1; 2 is 0b10; 4 is 0b100; 9 is 0b1001.
When the base is -2, it is the same logic.
9 = -2 * -4 + 1
-4 = -2 * 2 + 0
2 = -2 * -1 + 0
-1 = -2 * 1 + 1
1 = -2 * 0 + 1
Therefore, 9 is converted to 11001, the reverse of 10011.
