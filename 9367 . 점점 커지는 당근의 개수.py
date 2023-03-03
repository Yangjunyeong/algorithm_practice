T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    carrot_lst = list(map(int, input().split()))
    cnt = 1
    a = []
    max_sequence = 1
    for i in range(1, n):
        if carrot_lst[i] > carrot_lst[i - 1]:
            cnt += 1
        else:
            cnt = 1

        if cnt != 1 and max_sequence < cnt:
            max_sequence = cnt

    print(f'#{tc} {max_sequence}')