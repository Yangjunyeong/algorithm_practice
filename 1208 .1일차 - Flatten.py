for tc in range(1, 11):
    dump_n = int(input())
    height_lst = list(map(int, input().split()))
    cnt = 1
    while cnt <= dump_n:
        max_height = 0
        min_height = 0
        for idx in range(len(height_lst)):
            if height_lst[max_height] < height_lst[idx]:
                max_height = idx
            if height_lst[min_height] > height_lst[idx]:
                min_height = idx
        height_lst[max_height] -= 1
        height_lst[min_height] += 1
        cnt += 1
    m = height_lst[0]
    n = height_lst[0]
    for i in height_lst:
        if m < i:
            m = i
        if n > i:
            n = i

    print(f'#{tc} {m - n}')