T = int(input())
for _ in range(T):
    n = input()
    
    stack = []
    stack.append(n[0])
    for i in n:
        if stack[-1] != i:
            stack.append(i)
            
    
    print("".join(stack))
