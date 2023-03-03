T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
    a, b = map(int, input().split())

    visited = [0] * (V + 1)


    def dfs(z):
        visited[z] = 1
        for i in G[z]:
            if not visited[i]:
                dfs(i)


    dfs(a)
    print(f'#{tc} {visited[b]}')