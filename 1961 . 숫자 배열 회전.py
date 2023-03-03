def rotation_90_degrees(lst, n):
    lst_90 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            lst_90[i][j] = lst[n - 1 - j][i]
    return lst_90


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    turn90 = rotation_90_degrees(arr, N)
    turn180 = rotation_90_degrees(turn90, N)
    turn270 = rotation_90_degrees(turn180, N)

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(turn90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(turn180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(turn270[i][j], end='')
        print()