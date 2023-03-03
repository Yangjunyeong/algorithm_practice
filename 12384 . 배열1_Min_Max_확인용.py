T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst_N = list(map(int, input().split()))
    mx = 0

    for i in lst_N:  # 최대값
        if mx < i:
            mx = i

    mn = 10000000
    for i in lst_N:    # 최소값
        if mn > i:
            mn = i

    print(f"#{test_case} {mx - mn}")