dr = [-1, 0, 0]
dc = [0, -1, 1]
for tc in range(1, 11):
    n = int(input())
    d = 0
    r = 99
    lst = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    c = 0
    for i in range(102):
        if lst[99][i] == 2:
            c = i

    while True:
        if r == 0:
            break

        if lst[r][c - 1]:
            d = 1
            while True:

                r += dr[d]
                c += dc[d]
                if lst[r][c - 1] == 0:
                    break
        elif lst[r][c + 1]:
            d = 2
            while True:
                r += dr[d]
                c += dc[d]
                if lst[r][c + 1] == 0:
                    break
        d = 0
        r += dr[d]
        c += dc[d]

    print(f'#{n} {c - 1}')