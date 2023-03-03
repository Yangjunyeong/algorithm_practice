T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    M = len(A)
    N = len(B)
    i = cnt = 0

    while i <= M - N:
        r = ''
        key = 0
        for j in range(len(B)):
            if A[i + j] == B[j]:
                key += 1
            else:
                break
        if key == N:
            cnt += 1
            i += N

        else:
            cnt += 1
            i += 1

    print(f'#{tc} {cnt + M - i}')