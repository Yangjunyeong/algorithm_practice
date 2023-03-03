for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]
    counter = 0
    for r in range(8):
        for c in range(8 - n + 1):
            cnt = 0
            for i in range(n // 2):
                if arr[r][c + i] == arr[r][c + n - 1 - i]:
                    cnt += 1
            if cnt == n // 2:
                counter += 1
            cnt = 0
            for i in range(n // 2):
                if arr[c + i][r] == arr[c + n - 1 - i][r]:
                    cnt += 1
            if cnt == n // 2:
                counter += 1

    print(f'#{tc} {counter}')