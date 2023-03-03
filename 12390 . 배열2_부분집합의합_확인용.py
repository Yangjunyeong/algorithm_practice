T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    cnt = 0

    for i in range(1 << 12):
        sub = []
        sum_sub = 0
        for j in range(12):
            if i & (1 << j):
                sub.append(A[j])
                sum_sub += A[j]

        if len(sub) == N and sum_sub == K:
            cnt += 1

    print(f'#{tc} {cnt}')