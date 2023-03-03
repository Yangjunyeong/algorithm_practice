for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(100)]
    max_len = 0  # 최대길이 저장할 변수
    br_point = 0  # 멈춤 구간 설정
    for i in range(100, 0, -1):
        if br_point == 1:
            break
        for r in range(100):
            if br_point == 1:
                break
            for c in range(100 - i + 1):
                cnt = 0
                for j in range(i // 2):
                    if arr[r][c + j] == arr[r][c + i - 1 - j]:
                        cnt += 1
                if cnt == i // 2:
                    max_len = i
                    br_point = 1
                    break
                cnt = 0
                for j in range(i // 2):
                    if arr[c + j][r] == arr[c + i - 1 - j][r]:
                        cnt += 1
                if cnt == i // 2:
                    max_len = i
                    br_point = 1
                    break

    print(f'#{tc} {max_len}')