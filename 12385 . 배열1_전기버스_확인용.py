T = int(input())

for tc in range(1, T + 1):

    K, N, M = map(int, input().split())
    charge_station_lst = list(map(int, input().split()))  # 충전소리스트를 입력받습니다.

    now = 0  # 처음 출발 위치를 지정합니다.
    move_point = now + K  # 현재 위치에서 최대로 갈 수 있는 위치를 지정합니다.
    can_charge = 0  # 충전소의 위치를 저장할 변수를 지정합니다.
    cnt = 0  # 횟수를 셀 초기값을 설정합니다.

    while move_point < N:  # 최대로 갈 수 있는 위치가 정류장의 개수를 넘어가면 반복을 멈춥니다.
        # 최대로 갈 수 있는 위치가 마지막 정거장에 도착하면 끝이므로 끝값은 반복에 포함하지 않습니다.
        for i in charge_station_lst:
            if now < i <= move_point:  # 만약 충전소가 현재 위치 최대로 갈 수 있는 지점 사이에 있으면 그 충전소 위치를 저장합니다.
                can_charge = i
            elif i > move_point:  # 범위를 벗어나면 for 반복을 멈춥니다.
                break

        if can_charge == 0:
            cnt = 0
            break

        now = can_charge
        move_point = now + K
        cnt += 1
        can_charge = 0  # 충전소 위치가 없을 경우 while문 반목을 멈출 장치로 사용하기 위해 충전소 위치를 다시 초기화 합니다.

    print(f'#{tc} {cnt}')