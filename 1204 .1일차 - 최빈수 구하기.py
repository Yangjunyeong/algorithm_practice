T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    lst_score = list(map(int, input().split()))
    C = [0] * (100 + 1)

    for num in lst_score:
        C[100 - num] += 1

    max_frequency = C[0]
    for i in C:
        if max_frequency < i:
            max_frequency = i

    print(f'#{tc} {100 - C.index(max_frequency)}')