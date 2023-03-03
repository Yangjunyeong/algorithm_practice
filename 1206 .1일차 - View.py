for tc in range(1, 11):
    T = int(input())
    lst_building = list(map(int, input().split()))
    a = 0

    for i in range(2, T - 2):
        # 빌딩의 양쪽 두 칸에 제일 큰 빌딩의 길이를 측정
        b = [lst_building[i - 2], lst_building[i - 1], lst_building[i + 1], lst_building[i + 2]]
        max_side_building = lst_building[i - 2]
        for j in b[1:]:
            if max_side_building < j:
                max_side_building = j
        # 양 옆 두칸의 최대 높이의 건물과 현재 건물의 높이를 비교
        if lst_building[i] - max_side_building > 0:
            a += lst_building[i] - max_side_building
    print(f'#{tc} {a}')