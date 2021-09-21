class Solution:
    def merge(self, inte: List[List[int]]) -> List[List[int]]:
        inte.sort(key = lambda x:x[0])
        i = 0
        while i < len(inte) - 1:
            if inte[i][1] >= inte[i+1][1]:
                inte.pop(i+1)
            elif inte[i][1] >= inte[i+1][0]:
                inte[i][1] = inte[i+1][1]
                inte.pop(i+1)
            else:
                i += 1
        return inte 
