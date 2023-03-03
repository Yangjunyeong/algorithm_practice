T = int(input())

for tc in range(1, T + 1):
    deco_str = input()
    col_arr = 4 * len(deco_str) + 1
    arr = [[0] * col_arr for _ in range(5)]
    for c in range(col_arr):
        if c % 4 == 0:
            arr[0][c] = '.'
            arr[1][c] = '.'
            arr[2][c] = '#'
            arr[3][c] = '.'
            arr[4][c] = '.'
        elif c % 4 == 1 or c % 4 == 3:
            arr[0][c] = '.'
            arr[1][c] = '#'
            arr[2][c] = '.'
            arr[3][c] = '#'
            arr[4][c] = '.'
        elif c % 4 == 2:
            arr[0][c] = '#'
            arr[1][c] = '.'
            arr[2][c] = deco_str[c // 4]
            arr[3][c] = '.'
            arr[4][c] = '#'
    for i in range(5):
        print(''.join(arr[i]))
        