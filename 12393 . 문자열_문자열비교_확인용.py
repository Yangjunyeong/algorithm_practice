T = int(input())

for tc in range(1, T + 1):
    s1 = input()
    s2 = input()
    m = len(s1)
    n = len(s2)

    cnt = 0
    for i in range(n - m + 1):

        if s2[i:i + m] == s1:
            cnt = 1
            break
    if cnt == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')