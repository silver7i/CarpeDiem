def backtrack(depth, row, total_cost):
    global min_cost
    if total_cost >= min_cost:
        return

    if depth == N-1:
        if path[row][0] != 0:
            final_cost = total_cost + path[row][0]
            if min_cost > final_cost:
                min_cost = final_cost
        return

    for col in range(1, N):
        if visited[col] == 0 and path[row][col] != 0:
            visited[col] = 1
            backtrack(depth + 1, col, total_cost + path[row][col])
            visited[col] = 0


N = int(input())
path = [list(map(int, input().split())) for _ in range(N)]

min_cost = float("inf")

visited = [0] * N
visited[0] = 1

backtrack(0, 0, 0)

print(min_cost)
