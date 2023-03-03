T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst_n = list(input())

    cnt = 0
    max_sequence = 0
    for i in lst_n:
        if int(i):
            cnt += 1
        else:
            cnt = 0
        if cnt and max_sequence < cnt:
            max_sequence = cnt
    print(f'#{tc} {max_sequence}')



