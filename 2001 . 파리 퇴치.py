T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_lst = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            fly_sum = 0
            for i in range(M):
                for j in range(M):
                    fly_sum += fly_lst[r + i][c + j]
            if max_sum < fly_sum:
                max_sum = fly_sum

    print(f'#{tc} {max_sum}')