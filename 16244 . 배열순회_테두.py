T = int(input())

for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]

    r1, c1, n = map(int, input().split())

    for r in range(r1, r1 + n):
        for c in range(c1, c1 + n):
            if r == r1 or r == r1 + n - 1:
                arr[r][c] = 1

            else:
                if c == c1 or c == c1 + n - 1:
                    arr[r][c] = 1

    print(f'#{tc}')

    for i in arr:
        for j in i:
            print(j, end=' ')
        print()