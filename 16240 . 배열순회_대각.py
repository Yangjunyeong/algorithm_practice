T = int(input())

for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]

    r1, c1, n = map(int, input().split())

    cnt = 0
    for r in range(r1, r1 + n):
        arr[r][c1 + cnt] = 1
        arr[r][c1 + n - 1 - cnt] = 1
        cnt += 1

    print(f'#{tc}')

    for i in arr:
        for j in i:
            print(j, end=' ')
        print()