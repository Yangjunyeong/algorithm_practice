T = int(input())

for tc in range(1, T + 1):
    str_lst = input()
    a = len(str_lst)
    cnt = 0
    for i in range(a // 2):
        if str_lst[i] == str_lst[a - 1 - i]:
            cnt += 1

    if cnt == a // 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')