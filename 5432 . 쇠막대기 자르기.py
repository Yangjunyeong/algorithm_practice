T = int(input())

for tc in range(1, T + 1):
    lst = list(input())
    laser = 0
    stack = []
    cnt = 0
    for i in lst:
        if len(stack) == 0 and i == '(':
            stack.append(i)
        elif laser == 0:
            if stack[-1] == '(' and i == ')':
                laser = 1
                stack.pop()
                cnt += len(stack)
            else:
                stack.append(i)
        else:
            if i == '(':
                laser = 0
                stack.append(i)
            else:
                stack.pop()
                cnt += 1
    print(f'#{tc} {cnt}')