T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    result = ''
    for i in range(N):
        a, num = map(str, input().split())
        for j in range(int(num)):
            result += a
            if len(result) == 10:
                print(result)
                result = ''

    print(result)