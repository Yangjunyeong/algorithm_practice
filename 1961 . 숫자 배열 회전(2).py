def turn_90(a):
    turn = zip(*a[::-1])
    return [list(e) for e in turn]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans1 = turn_90(arr)
    ans2 = turn_90(ans1)
    ans3 = turn_90(ans2)

    print(f'#{tc}')
    for r in range(n):
        for c in range(n):
            print(ans1[r][c], end='')
        print(end=" ")
        for c in range(n):
            print(ans2[r][c], end='')
        print(end=" ")
        for c in range(n):
            print(ans3[r][c], end='')
        print()