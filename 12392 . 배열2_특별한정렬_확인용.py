def sortsearch(a, m):
    for i in range(m):
        maxidx = i
        minidx = i
        if i % 2 == 0:

            for j in range(i + 1, m):
                if a[maxidx] < a[j]:
                    maxidx = j
            a[i], a[maxidx] = a[maxidx], a[i]

        else:

            for j in range(i + 1, m):
                if a[minidx] > a[j]:
                    minidx = j
            a[i], a[minidx] = a[minidx], a[i]

    return a


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    result = sortsearch(lst, n)

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(result[i], end=' ')
    print()