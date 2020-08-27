n=int(input("enter the number: "))
for row in range (0,n):
    for col in range (0,n):
        if row==0 or row-col==0 or col == n-1:
            print("* ",end="")
        else:
            print(end="  ")
    print()