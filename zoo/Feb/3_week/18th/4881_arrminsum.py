def dfs(row, current_val):
    global min_val

    if current_val >= min_val:
        return
    
    if row == n:
        min_val = min(current_val, min_val)
        return
    
    for col in range(n):
        if not visited[col]:
            visited[col] = True

            dfs(row + 1, current_val + graph[row][col])

            visited[col] = False

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    visited = [False] * n
    graph = [list(map(int, input().split())) for _ in range(n)]

    min_val = int(1e9)

    dfs(0, 0)
    
    print(f"#{tc} {min_val}")