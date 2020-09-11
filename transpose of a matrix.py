m=[]
for i in range(3):
    a=[]
    for j in range(3):
        j=int(input("Enter the number in 1st matrix  ["+str(i)+"] ["+str(j)+"] : "))
        a.append(j)
    m.append(a)

print("Matrix is.......")
for i in range(3):
    for j in range(3):
        print(m[i][j],end=" ")
    print()

t=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        t[i][j]=m[j][i]

print("Transpose of Matrix is .......")
for i in range(3):
    for j in range(3):
        print(t[i][j],end=" ")
    print()

