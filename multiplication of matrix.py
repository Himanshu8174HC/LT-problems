m=[]
for i in range(3):
    a=[]
    for j in range(3):
        j=int(input("Enter the number in 1st matrix  ["+str(i)+"] ["+str(j)+"] : "))
        a.append(j)
    m.append(a)

n=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("Enter the number in 2nd matrix ["+str(i)+"] ["+str(j)+"] : "))
        b.append(j)
    n.append(b)

print("First Matrix is.......")
for i in range(3):
    for j in range(3):
        print(m[i][j],end=" ")
    print()

print("Second Matrix is.......")
for i in range(3):
    for j in range(3):
        print(n[i][j],end=" ")
    print()

result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] = result[i][j] + m[i][k] * n[k][j]

print("Resultant matrix is .........")
for i in range(3):
    for j in range(3):
        print(result[i][j], end=" ")
    print()
