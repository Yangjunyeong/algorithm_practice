T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    price_lst = list(map(int, input().split()))

    max_price = price_lst[-1]
    benefit = 0
    for i in range(n - 1, -1, -1):
        if max_price >= price_lst[i]:
            benefit += max_price - price_lst[i]
        elif max_price < price_lst[i]:
            max_price = price_lst[i]

    print(f'#{tc} {benefit}')