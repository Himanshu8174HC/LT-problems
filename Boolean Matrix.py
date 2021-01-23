def booleanMatrix(matrix):
    # code here 
    ROW = [0]*len(matrix)
    COLUMN = [0]*len(matrix[0])
    
    

    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == 1:
                ROW[i] = 1
                COLUMN[j] = 1
                
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if ROW[i] ==1 or COLUMN[j] ==1:
                matrix[i][j] =1
                
    return matrix
