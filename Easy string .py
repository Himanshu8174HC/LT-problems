T = int(input())
for _ in range(T):
    n = input()
    n = n.lower()
    stack = []
    for i in n:
        if len(stack) == 0:
            stack.append(1)
            stack.append(i)
        elif stack[-1] == i:
            stack[-2]+=1
        else:
            stack.append(1)
            stack.append(i)
    print("".join(str(i) for i in stack))
