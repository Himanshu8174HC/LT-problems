a=int(input("Enter No of rows :"))
b=int(input("Enter no of column :"))
matrix=[]
for i in range(a):
    c=[]
    for i in range(b):
        j=int(input("Enter first matrix number :"))
        c.append(j)
    print()
    matrix.append(c)
matrix_1=[]
for i in range(a):
    d=[]
    for i in range(b):
        j=int(input("Enter second matrix number :"))
        d.append(j)
    print()
    matrix_1.append(d)
print("1st Matrix")
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()
print("2nd Matrix")
for i in range(a):
    for j in range(b):
        print(matrix_1[i][j],end=" ")
    print()

result=[[0]*b]*a
for i in range(a):
    for j in range(b):
        result[i][j]=matrix[i][j]+matrix_1[i][j]

print("Resultant Matrix......")
for i in range(a):
    for j in range(b):
        print(result[i][j],end=" ")
    print()
