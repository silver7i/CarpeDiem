def dfs(curr):  # 현재 노드 위치를 인자로 받으며 현재 노드 방문 표시 함수
    visited[curr] = 1  # 현재 노드위치 방문했다고 표시

    if curr == 99:  # 현재 위치가 99가 되면 함수 종료
        return

    for nxt in adj_list[curr]:  # 현재 노드 인접리스트를 반복
        if visited[nxt] == 0:  # 다음 노드를 방문한 적이 없다면
            dfs(nxt)  # 다음 노드를 현재 노드로 보냄


for _ in range(10):
    tc, E = map(int, input().split())  # tc 테스트 케이스의 번호, E 간선 수

    edges = list(map(int, input().split()))  # u와 v의 순서쌍

    adj_list = [[] for _ in range(100)]  # 0 ~ 99 의 노드 인접리스트

    for i in range(E):
        u, v = edges[i * 2], edges[i * 2 + 1]
        adj_list[u].append(v)

    visited = [
        0
    ] * 100  # 0~99 idx를 갖는 방문리스트 생성 _ 99를 방문했다면 visited[99] = 1 일 것이고 안했다면 0일 것임

    dfs(0)
    print(f"#{tc} {visited[99]}")
