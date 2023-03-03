T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = [2, 3, 5, 7, 11]
    a = []

    for i in lst:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        a.append(cnt)

    print(f'#{tc}', end=' ')
    for i in a:
        print(i, end=' ')
    print()