T = int(input())

for tc in range(1, T + 1):
    tc_input, a = map(str, input().split())
    n = int(a)
    dict_gns = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0,
                'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    num_lst = input().split()
    r = ''

    for i in num_lst:
        dict_gns[i] += 1

    for k, v in dict_gns.items():
        r += (k + ' ') * v

    print(f'#{tc} {r}')