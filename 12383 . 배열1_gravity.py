T = int(input())  # 테스트케이스 입력

for i in range(1, T + 1):
    N = int(input())
    box_lst = list(map(int, input().split()))
    a = []
    for j in range(N):
        cnt = N - j

        for h in range(j, N):

            if box_lst[h] >= box_lst[j]:
                cnt -= 1

        a.append(cnt)
    max_height = a[0]
    for h in a:
        if h > max_height:
            max_height = h

    print(f'#{i} {max_height}')