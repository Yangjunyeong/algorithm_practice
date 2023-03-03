T = int(input())

for tc in range(1, T + 1):
    sdo_lst = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    for r in range(9):
        a = set()
        for c in range(9):
            a.add(sdo_lst[r][c])

        if len(a) == 9:
            cnt += 1

        else:
            break

    for r in range(9):
        a = set()
        for c in range(9):
            a.add(sdo_lst[c][r])

        if len(a) == 9:
            cnt += 1

        else:
            break

    for r in range(9):
        a = set()
        for c in range(9):
            if r % 3 == 0 and c % 3 == 0:
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        a.add(sdo_lst[i][j])
                if len(a) == 9:
                    cnt += 1
                else:
                    break

    if cnt == 27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')