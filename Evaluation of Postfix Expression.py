t = int(input())
for _ in range(t):
    n = input()
    stack = []
    ls = ['+', '-','*','/']
    for i in n:
        if i not in ls:
            stack.append(str(i))
        else:
            b = stack.pop()
            a = stack.pop()
        if (i ==str('*')):
            stack.append(int(a)*int(b))
        elif (i ==str('/')):
            stack.append(int((int(a)/int(b))))
        elif (i ==str('+')):
            stack.append(int(a)+int(b))
        elif (i ==str('-')):
            stack.append(int(a)-int(b))
    if len(stack) ==1:
        print(stack[0])
    else:
        print('-1')
