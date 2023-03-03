T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    a = []

    for i in range(N - M + 1):  # 구간 합 만들기
        b = 0
        for j in range(M):
            b += lst[i + j]
        a.append(b)

    max_neighbor = a[0]
    min_neighbor = a[0]

    for i in range(len(a)):
        if a[i] > max_neighbor:
            max_neighbor = a[i]
        if a[i] < min_neighbor:
            min_neighbor = a[i]

    print(f'#{test_case + 1} {max_neighbor - min_neighbor}')