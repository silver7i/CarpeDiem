def dfs(curr):
    stack = []  # 스택 생성
    visited[curr] = 1  # 현재 위치 방문 기록 남기기

    for nxt in adj_list[curr]:
        if visited[nxt] == 0:
            dfs(nxt)

    return visited


V = int(input())  # V 컴퓨터 수
E = int(input())  # 간선 수

adj_list = [[] for _ in range(V + 1)]  # 1~V 만큼 쓸거임

# 직접 연결되어 있는 컴퓨터 번호 쌍 E개만큼
for _ in range(E):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)  # 양방향이라

# 출력 -> 1번 컴퓨터가 바이러스 일때 바이러스에 걸리게 되는 컴퓨터의 수
"""
dfs(curr) 함수 만들어서 방문 기록 남기기 -> 1의 개수가 바이러스 걸린 컴퓨터 수
"""
visited = [0] * (V + 1)

dfs(1)
print(visited.count(1) - 1)
