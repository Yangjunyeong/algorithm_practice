T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    str_l = [input() for _ in range(N)]
    a = ''
    for r in range(N):
        for c in range(N - M + 1):
            cnt = 0
            for i in range(M // 2):
                if str_l[r][i + c] == str_l[r][c + M - 1 - i]:
                    cnt += 1
            if cnt == M // 2:
                a += str_l[r][c:c + M]

    for r in range(N):
        for c in range(N - M + 1):
            cnt = 0
            s = ''
            for i in range(M // 2):
                if str_l[c + i][r] == str_l[c + M - 1 - i][r]:
                    cnt += 1
            if cnt == M // 2:
                for j in range(M):
                    s += str_l[c + j][r]
                a += s

    print(f'#{tc}', end=' ')
    print(a)