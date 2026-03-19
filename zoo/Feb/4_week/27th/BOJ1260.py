def dfs(v):
    stack = []
    visited = [0] * (N+1)
    visited[v] = 1
    curr_v = v
    print(curr_v, end = " ")

    while True:
        for nxt_v in adj_list[curr_v]:
            if visited[nxt_v] == 0:
                stack.append(curr_v)
                visited[nxt_v] = 1
                print(nxt_v, end = " ")
                curr_v = nxt_v
                break
        else:
            if stack:
                curr_v = stack.pop()
            else:
                break


def bfs(v):
    queue = [v]
    visited = [0] * (N+1)
    visited[v] = 1
    front = 0
    while front < len(queue):
        curr_v = queue[front]
        front += 1
        print(curr_v, end = " ")
        for nxt_v in adj_list[curr_v]:
            if visited[nxt_v] == 0:
                queue.append(nxt_v)
                visited[nxt_v] = 1

# 입력 : N 정점의 개수, M 간선의 개수, V 시작할 정점의 번호

# 출력 : 첫째줄 DFS, 둘째줄 BFS 
# 단, 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문

N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for a in adj_list:
    a.sort()

dfs(V)
print()
bfs(V)
