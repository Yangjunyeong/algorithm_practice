def nemo_counting(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        result = nemo_counting(n - 1) + 2 * nemo_counting(n - 2)
        return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input()) // 10
    print(f'#{tc} {nemo_counting(N)}')