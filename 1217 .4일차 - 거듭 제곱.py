def involution_cal(n, m):
    if m == 1:
        return n
    elif m == 0:
        return 1
    else:
        return n * involution_cal(n, m - 1)


for tc in range(1, 11):
    t = int(input())
    N, M = map(int, input().split())
    print(f'#{tc} {involution_cal(N, M)}')