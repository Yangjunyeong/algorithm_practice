T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst_n = list(map(int, input().split()))
    count = [0] * (50 + 1)

    for num in lst_n:
        count[num] += 1
    b = []
    for i, j in enumerate(count):
        if j:
            for h in range(j):
                b.append(i)
    print(f"#{tc}", end=' ')
    for i in b:
        print(i, end=' ')
    print()