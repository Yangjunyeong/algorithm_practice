def stack_zero(a, N):
    top = -1
    s = [0] * N
    for i in a:

        if i:
            top += 1
            s[top] = i
        else:
            if top >= 0:
                s[top] = 0
                top -= 1
            else:
                top = -1

    sum_stack = 0
    for i in s:
        sum_stack += i
        if i == 0:
            break

    return sum_stack


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    print(f'#{tc} {stack_zero(lst, n)}')