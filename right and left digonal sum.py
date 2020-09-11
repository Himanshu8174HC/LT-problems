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

print("Matrix is.....")
for i in range(3):
    for j in range(3):
        print(m[i][j],end="  ")
    print()

sum_L_D=0
sum_R_D=0
for i in range(3):
    for j in range(3):
        if i==j:
            sum_L_D+=m[i][j]
        if i+j==3-1:
            sum_R_D+=m[i][j]

print("Left Digonal Sum is :",sum_L_D)
print("Rightt Digonal Sum is :",sum_R_D)
