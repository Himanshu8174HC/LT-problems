m=[]
row=0
column=0
r=[]
c=[]
for i in range(3):
    a=[]
    for j in range(3):
        j=int(input("Enter the number in matrix  ["+str(i)+"] ["+str(j)+"] : "))
        a.append(j)
    m.append(a)

for i in range(3):
    for j in range(3):
        row=row+m[i][j]
        column=column+m[j][i]
    r.append(row)
    c.append(column)
    row=0
    column=0

for i in range(3):
    for j in range(3):
        print(m[i][j],end="  ")
    print(r[i],end=" ")
    print()

for i in range(3):
    print(c[i],end=" ")
