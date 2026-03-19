def bfs(S):
    queue = []

    visited[S] = 1

    queue.append(S)

    while queue:
        curr_nod = queue.pop(0)

        for nxt_nod in adj_list[curr_nod]:
            if visited[nxt_nod] == 0:
                visited[nxt_nod] = visited[curr_nod] + 1
                queue.append(nxt_nod)
    
    return visited


t = int(input())

for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    S, G = map(int, input().split())

    # 출력: S에서 G로 가는 경우, 몇개의 간선을 지나야하는가
    # 서로 연결되어 있지 않다면, 0을 출력함.

    """
    필요한것
    S: 출발 노드, G: 도착 노드
    V: 노드 수, E: 간선 수
    visited = [0] * (V + 1)
    """
    visited = [0] * (V+1)
    bfs(S)
    if visited[G] != 0:
        print(f"#{tc} {visited[G]-1}")
    else:
        print(f"#{tc} {visited[G]}")