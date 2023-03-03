T = int(input())

for tc in range(1, T + 1):
    str_lst = list(input())
    s = []
    for i in str_lst:
        if len(s) == 0:
            s.append(i)
        elif s[-1] == i:
            s.pop()
        else:
            s.append(i)

    result = len(s)
    print(f'#{tc} {result}')