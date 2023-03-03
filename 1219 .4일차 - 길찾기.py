for tc in range(10):
    n, E = map(int, input().split())
    G = [[] for _ in range(100)]

    route_lst = list(map(int, input().split()))
    for i in range(0, 2 * E, 2):
        u, v = route_lst[i], route_lst[i + 1]
        G[u].append(v)

    visited = [0] * 100


    def dfs(s):
        visited[s] = 1
        if s == 99:
            return

        for i in G[s]:
            if not visited[i]:
                dfs(i)


    dfs(0)

    print(f'#{n} {visited[99]}')