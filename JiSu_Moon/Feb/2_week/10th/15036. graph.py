# 그래프 경로


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b)

    S, G = map(int, input().split())
    visited = [0] * (V+1)

    def dfs(v):
        visited[v] = 1
        
        for i in graph[v]:
            if visited[i] == 0:
                dfs(i)

    dfs(S)

    if visited[G]:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")