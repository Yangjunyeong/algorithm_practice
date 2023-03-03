T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for j in range(r1, r2 + 1):
            for h in range(c1, c2 + 1):
                arr[j][h] += 1

    cnt = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] > 1:
                cnt += 1

    print(f'#{tc} {cnt}')