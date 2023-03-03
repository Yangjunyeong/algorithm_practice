T = int(input())

for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]

    r1, c1, wei, hei = map(int, input().split())

    cnt = 1
    for r in range(r1, r1 + hei):
        for c in range(c1, c1 + wei):
            if (r - r1) % 2:
                arr[r][c1 + wei - 1 - (c - c1)] = cnt
                cnt += 1
            else:
                arr[r][c] = cnt
                cnt += 1

    print(f'#{tc}')

    for i in arr:
        for j in i:
            print(j, end=' ')
        print()