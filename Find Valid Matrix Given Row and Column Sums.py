class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        m = [[0 for i in range(len(colSum))] for i in range(len(rowSum))]
        
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                temp  = min(rowSum[i], colSum[j])
                m[i][j] = temp
                rowSum[i] -= temp
                colSum[j] -= temp
        return m


                
        
