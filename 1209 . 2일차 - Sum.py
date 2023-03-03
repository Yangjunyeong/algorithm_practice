for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum_r = 0
    for r in range(100):
        sum_arr = 0
        for c in range(100):
            sum_arr += arr[r][c]

        if max_sum_r < sum_arr:
            max_sum_r = sum_arr

    max_sum_c = 0
    for c in range(100):
        sum_arr = 0
        for r in range(100):
            sum_arr += arr[r][c]

        if max_sum_c < sum_arr:
            max_sum_c = sum_arr

    sum_d = 0
    sum_rd = 0
    for r in range(100):
        sum_d += arr[r][r]
        sum_rd += arr[r][100 - r - 1]

    a = [max_sum_r, max_sum_c, sum_d, sum_rd]
    real_max = 0
    for i in a:
        if real_max < i:
            real_max = i

    print(f'#{t} {real_max}')
