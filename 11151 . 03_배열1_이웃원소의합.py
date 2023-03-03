T = int(input())  # 테스트케이스 입력

for i in range(1, T + 1):
    N = int(input())
    n_lst = list(map(int, input().split()))
    sum_lst = []  # 구간합 리스트의 초기값을 설정
    # 각 구간합을 구하거 구간합의 리스트에 계속 추가
    for j in range(0, N - 2 + 1):
        sum_part = 0
        for h in range(2):
            sum_part += n_lst[j + h]
        sum_lst.append(sum_part)
    # 구간합 리스트에서 최대값을 구하기
    max_sum = sum_lst[0]
    for m in sum_lst:
        if m > max_sum:
            max_sum = m

    print(f'#{i} {max_sum}')