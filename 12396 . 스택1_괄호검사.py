T = int(input())

for tc in range(1, T + 1):
    str_lst = list(input())
    s = []
    stack = []
    paren = ['(', '{', ')', '}']
    for i in str_lst:
        if i in paren:
            s.append(i)
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == '{' and i == '}':
            stack.pop()
        elif stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')