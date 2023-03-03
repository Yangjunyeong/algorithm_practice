T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for i in range(N):
        a, b = map(int, input().split())
        lst.append((a, b))

    p = int(input())
    P_lst = []
    for i in range(p):
        c = int(input())
        P_lst.append(c)

    cnt = [0] * 5001

    for i in range(len(lst)):
        for j in set(P_lst):
            if lst[i][0] <= j <= lst[i][1]:
                cnt[j] += 1
    print(f'#{tc}', end=' ')
    for i in P_lst:
        print(cnt[i], end=' ')
    print()
