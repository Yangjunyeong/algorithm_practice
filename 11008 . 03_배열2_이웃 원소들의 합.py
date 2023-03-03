dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mx = 0

    for r in range(n):
        for c in range(n):
            neighbor_sum = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < n and 0 <= nc < n:
                    neighbor_sum += arr[nr][nc]
            if mx < neighbor_sum:
                mx = neighbor_sum
                idx = (r, c)
    print(f'#{tc}', idx[0], idx[1], mx)