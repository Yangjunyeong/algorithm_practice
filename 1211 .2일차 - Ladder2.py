for tc in range(1, 11):
    n = int(input())
    d = r = c = 0
    lst = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    min_route = 100000000
    min_idx = 0

    for i in range(102):
        if lst[0][i] != 1:
            continue
        cnt = 0
        r = 0
        c = i
        while r != 99:
            cnt += 1
            if d == 0:
                if lst[r][c - 1]:
                    d = 1
                    c -= 1
                elif lst[r][c + 1]:
                    d = 2
                    c += 1
                else:
                    r += 1
            else:
                if d == 1 and lst[r][c - 1]:
                    c -= 1

                elif d == 2 and lst[r][c + 1]:
                    c += 1
                else:
                    d = 0
                    r += 1

        if min_route > cnt:
            min_route = cnt
            min_idx = i

    print(f'#{n} {min_idx - 1}')