n=input("enter the number:")
ans=0
for i in n:
    ans=ans+int(i)**len(n)
if ans==int(n):
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")


print(ans)
    