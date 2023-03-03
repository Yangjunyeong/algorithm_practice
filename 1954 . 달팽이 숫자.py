T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = [[0] * n for _ in range(n)]
    cnt = 0
    x = -1
    y = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir_k = 0
    while cnt < n ** 2:
        nx = x + dx[dir_k]
        ny = y + dy[dir_k]
        if 0 <= nx < n and 0 <= ny < n and lst[ny][nx] == 0:
            cnt += 1
            lst[ny][nx] = cnt
            x, y = nx, ny
        else:
            dir_k += 1
            dir_k = dir_k % 4

    print(f'#{tc}')
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()