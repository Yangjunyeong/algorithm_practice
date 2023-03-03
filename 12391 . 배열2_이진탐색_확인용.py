def binary_search(entire_page, find_page):
    start = 1
    end = entire_page
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        if middle == find_page:
            cnt += 1
            return cnt
        elif middle > find_page:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1


T = int(input())

for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    a = binary_search(P, A)
    b = binary_search(P, B)

    if a < b:
        print(f'#{tc} A')
    elif a > b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')