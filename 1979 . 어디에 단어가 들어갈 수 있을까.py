def count(a):
    ans = 0
    for lst in a:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1
            else:
                if cnt == M:
                    ans += 1
                cnt = 0
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]
    arr_t = list(list(zip(*arr)))
    result = count(arr) + count(arr_t)

    print(f'#{tc} {result}')