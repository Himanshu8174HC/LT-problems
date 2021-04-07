class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        Amax = 0
        for i in range(len(A) - 2):
            Amax = max(Amax, A[i])
            if Amax > A[i + 2]:
                return False
        return True
