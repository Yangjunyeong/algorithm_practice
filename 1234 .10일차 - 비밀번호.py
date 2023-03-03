for tc in range(1, 11):
    n, arr = map(str, input().split())
    str_lst = list(arr)
    result = []

    for i in str_lst:
        if len(result) == 0:
            result.append(i)
        elif result[-1] == i:
            result.pop()
        else:
            result.append(i)
    print(f'#{tc}', end=' ')

    print("".join(result))