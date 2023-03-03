T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    M = len(A)
    N = len(B)
    i = 0
    cnt = 0
    while i < M:
        cnt += 1
        if A[i] == B[0] and A[i:i + N] == B:
            i += N
        else:
            i += 1
    print(f'#{tc}', cnt)