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

print("Lower Triangular of Matrix is .......")
for i in range(3):
    for j in range(3):
        if i>j:
            print(m[i][j],end=" ")
    print()

print("Upper Triangular of Matrix is .......")
for i in range(3):
    for j in range(3):
        if j>i:
            print(m[i][j],end=" ")
    print()
