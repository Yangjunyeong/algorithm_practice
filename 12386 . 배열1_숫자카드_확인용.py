T = int(input())  # 테스트케이스 입력

for tc in range(1, T + 1):
    N = int(input())
    lst_n = list(map(int, list(input())))
    C = [0] * (9 + 1)

    for i in lst_n:
        C[9 - i] += 1

    max_frequency = C[0]
    for i in C:
        if max_frequency < i:
            max_frequency = i

    print(f'#{tc} {9 - C.index(max_frequency)} {max_frequency}')